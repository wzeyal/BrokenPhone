import dash
from dash import dcc, html

dash.register_page(__name__)

game_pin = 123456

# layout = html.Div(
#     [
#         dcc.Markdown(f'# {game_pin}'),
#         dcc.Markdown(f'## Should be a list of pictures'),
#         dcc.Link(html.Button("Create again"), href="/",)
#     ]
# )

layout = html.Div(
    [
        html.Div('10% Top', style={'height': '10%', 'text-align': 'center', 'background-color': 'red'}),
        html.Div(
            [
                dcc.Markdown(f'# {game_pin}'),
            ],
            '80% Middle',
            style={'height': '80%', 'text-align': 'center', 'background-color': 'green'}
        ),
        html.Div('10% Bottom', style={'height': '10%', 'text-align': 'center', 'background-color': 'red'})
    ],
    style={'display': 'flex', 'flex-direction': 'column', 'height': '90vh'}
)