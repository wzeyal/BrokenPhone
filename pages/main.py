import dash
from dash import dcc, html

dash.register_page(__name__, path='/')


class MainView:
    def __init__(self):
        self.layout = dcc.Link(html.Button("Create Game", id="create_game",), href="/upload", )


layout = MainView().layout
