import dash
import dash_bootstrap_components as dbc
from dash import dcc

from pages.base import BasePage

# dash.register_page(__name__, path="/")


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.layout = dcc.Link(dbc.Button("Create Gam2e", id="create_game", color="Primary"), href="/upload",
                               style={'margin-top': '25vh'})


layout = MainPage().layout
