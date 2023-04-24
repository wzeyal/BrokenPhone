import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path='/test')


class TestView:
    def __init__(self):
        self.layout = dbc.Container([
            # Header row
            dbc.Row(
                dbc.Col(
                    html.H1("My Dashboard"),
                    width={'size': 8, 'offset': 4},
                    style={'text-align': 'center'}
                ),
                # style={'margin-top': '50px'}
                style={
                    'position': 'fixed',
                    'top': 0,
                    'left': 0,
                    'width': '100%',
                    'background-color': 'white',
                    'z-index': 9999
                }

            ),
            # Body row
            dbc.Row(
                dbc.Col(
                    html.Div("This is the body of my dashboard"),
                    width={'size': 6, 'offset': 3},
                    style={'height': '60vh', 'overflow': 'auto'}
                ),
                style={'margin-top': '50px'}
            ),
            # Footer row
            dbc.Row(
                dbc.Col(
                    html.P("Copyright © 2023 My Company"),
                    width={'size': 6, 'offset': 3},
                    style={'text-align': 'center'}
                ),
                style={'margin-top': '50px'}
            )
        ],
            style={
                # Apply landscape styles when screen width is greater than height
                '@media (min-aspect-ratio: 1/1)': {
                    'height': '100vh',
                    'max-height': '100vw',
                    'overflow-x': 'hidden'
                }
            }
        )


layout = TestView().layout
