import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
dash.register_page(__name__, path='/')


class MainView:
    def __init__(self):
        self.layout = dcc.Link(dbc.Button("Create Gam2e", id="create_game", color="Primary"), href="/upload",
                               style={'margin-top': '25vh'})


layout = MainView().layout
