import threading
import time

from bit import Key
from dash import Dash, Input, Output, State, html, dcc
from constants_app import PUZZLES_LIST, DF, NB_THREAD
import random

server = Dash(__name__)

hex_count = 0
start_time = time.perf_counter()
calculation_thread = None
output_value = ""

server.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.H1('BTC Puzzle Solver', className="title")
        ]
    ),
    html.Div(
        className="div-choix",
        children=[
            html.H3('Choose puzzle : '),
            dcc.Dropdown(
                id='dropdown',
                className="app-dropdown",
                options=PUZZLES_LIST,
                value=PUZZLES_LIST[0],  # Valeur par défaut
                clearable=False
            ),
            html.H3('Choose method : '),
            dcc.Dropdown(
                id='solving_method',
                className="method_solving",
                options=['Sequential', 'Random', 'Hybrid'],
                value='Random',  # Valeur par défaut
                clearable=False
            ),
            html.H3('Choose nb cpu core: '),
            dcc.Dropdown(
                id='cpu_count',
                className="nb_core",
                options=list(range(1, NB_THREAD + 1)),
                value=NB_THREAD,  # Valeur par défaut
                clearable=False
            ),
            html.Button('Start solving', id='submit-button', className="button-submit", n_clicks=0),
            html.Div(id="solving-speed-print", className="speed-print"),
            html.Div(id='progress-update'),
            html.Div(id='progress-output'),
            html.Div(id='progress-update2'),
            dcc.Interval(
                id='interval-component',
                interval=1 * 1000,  # in milliseconds
                n_intervals=0
            )
        ]
    ),
    html.Div(
        children=html.Div(
            className="footer",
            children=[
                html.P(
                    "Cette application résout les puzzles bitcoin",
                    className="explication"
                ),
            ])
    )
])


def format_keys_per_second(kps):
    if kps < 1e3:
        return f"{kps:.2f}"
    elif kps < 1e6:
        return f"{kps / 1e3:.2f}K"
    elif kps < 1e9:
        return f"{kps / 1e6:.2f}M"
    else:
        return f"{kps / 1e9:.2f}B"


def generate_output(start_range, end_range, target_address, output_file):
    global hex_count
    global start_time
    global output_value

    while True:
        i = random.randint(start_range, end_range)
        priv_key_hex = format(i, 'x').zfill(64)
        key = Key.from_hex(priv_key_hex)
        address = key.address

        hex_count += 1

        if address == target_address:
            print(f'\nPrivate Key: {priv_key_hex}, Address: {address}')
            result_string = f'!!!! FOUNDED !!!!\nPrivate Key: {priv_key_hex}, Address: {address}\n'
            output_value = result_string
            with open(output_file, 'a') as f:
                f.write(result_string)
            time.sleep(3600)
            break

        if hex_count % 100000 == 0:
            elapsed_time = time.perf_counter() - start_time
            elapsed_time = elapsed_time if elapsed_time > 0 else 1
            formatted_time = f'{int(elapsed_time // 3600)}:{int((elapsed_time % 3600) // 60):02d}:{int(elapsed_time % 60):02d}'
            formatted_hex_count = f'{hex_count:,}'.replace(',', '.')
            keys_per_second = hex_count / elapsed_time
            formatted_kps = format_keys_per_second(keys_per_second)

            display_key_hex = priv_key_hex.lstrip('0')
            display_key_hex = display_key_hex if display_key_hex else '0'

            output_value = f'[Scanned {formatted_hex_count} keys in {formatted_time}] [{formatted_kps} Keys/s.] [Current Hex: {display_key_hex}]'


@server.callback(
    Output('progress-update', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_progress(n):
    return output_value


@server.callback(
    Output('progress-output', 'children'),
    Input('dropdown', 'value'),
)
def display_solution(numero_puzzle: int):
    # print(numero_puzzle)
    df_ligne_puzzle = DF.loc[DF.puzzle_number == numero_puzzle]
    hexa = str(df_ligne_puzzle.hex.iloc[0])
    start_key = str(df_ligne_puzzle.start_key.iloc[0])
    stop_key = str(df_ligne_puzzle.stop_key.iloc[0])
    start_range = int(start_key, 16)
    stop_range = int(stop_key, 16)
    affichage = [
        html.H3("Numéro puzzle : " + str(numero_puzzle)),
        html.H3("Target : " + str(hexa)),
        html.H3("Start range : " + str(start_range)),
        html.H3("End range : " + str(stop_range))
    ]
    return affichage

@server.callback(
    Output('progress-update2', 'children'),
    Input('submit-button', 'n_clicks'),
    State('dropdown', 'value'),
    prevent_initial_call=True
)
def start_calculation(n_clicks, selected_puzzle):
    global hex_count
    global start_time
    global calculation_thread

    if n_clicks > 0 and calculation_thread is None:
        df_ligne_puzzle = DF.loc[DF.puzzle_number == selected_puzzle]
        hexa = str(df_ligne_puzzle.hex.iloc[0])
        start_key = str(df_ligne_puzzle.start_key.iloc[0])
        stop_key = str(df_ligne_puzzle.stop_key.iloc[0])
        start_range = int(start_key, 16)
        stop_range = int(stop_key, 16)
        output_file = "output.txt"
        calculation_thread = threading.Thread(target=generate_output, args=(start_range, stop_range, hexa, output_file), daemon=True)
        calculation_thread.start()


if __name__ == '__main__':
    server.run_server(debug=True)
