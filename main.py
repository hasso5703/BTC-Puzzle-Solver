from dash import Dash, Input, Output, State, html, dcc


"""
===========================================================================
application
"""
application = Dash(__name__)

"""
===========================================================================
pied de page
"""

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
            html.H3('Choisir puzzle : '),
            dcc.Dropdown(
                id='dropdown',
                className="app-dropdown",
                options=['a', 'b', 'x'],
                value='option1'  # Valeur par défaut
            ),
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

"""
===========================================================================
lancement du serveur
"""
if __name__ == '__main__':
    application.run_server(debug=True)
