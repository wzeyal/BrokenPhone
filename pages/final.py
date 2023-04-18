import dash
from dash import dcc, html

dash.register_page(__name__)

game_pin = 123456

layout = html.Div(
    [
        dcc.Markdown(f'# {game_pin}'),
    ]
)
