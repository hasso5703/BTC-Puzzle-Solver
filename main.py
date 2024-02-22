from dash import Dash, Input, Output, State, html, dcc
from constants_app import PUZZLES_LIST, DF, NB_THREAD


application = Dash(__name__)

application.layout = html.Div([
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
            dcc.Interval(
                id='interval-component',
                interval=1 * 1000,  # in milliseconds
                n_intervals=0
            ),
            html.Div(id='progress-output'),
            html.Div(id='result-output')
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


if __name__ == '__main__':
    application.run_server(debug=False)
