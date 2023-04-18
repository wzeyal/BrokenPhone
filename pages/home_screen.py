import dash
from dash import dcc, html

dash.register_page(__name__, path='/')

layout = html.Div(
    [
        # dcc.Markdown(f'# {__name__}'),
        html.Button('Create Game', id='create', n_clicks=0),
    ]
)
