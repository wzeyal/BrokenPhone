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

# layout = html.Div(
#     [
#         html.Div('10% Top', style={'height': '10vh', 'text-align': 'center', 'background-color': 'red'}),
#         html.Div(
#             [
#                 dcc.Markdown(f'# {game_pin}'),
#             ],
#             '80% Middle',
#             style={'height': '70vh', 'text-align': 'center', 'background-color': 'green'}
#         ),
#         html.Div('10% Bottom', style={'height': '10vh', 'text-align': 'center', 'background-color': 'red'})
#     ],
#     style={'display': 'flex', 'flex-direction': 'column', }
# )

layout = html.Div(
    style={'align-items': 'center', 'justify-content': 'center'},
    # 'display': 'flex', 'flex-direction': 'column'
    children=[
        html.Div([
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
            html.Img(src='https://via.placeholder.com/150x150'),
        ],
            className='centered-div',
            style={'height': '70vh', 'overflow-y': 'auto', },

            # style={'height': '70vh', 'overflow-y': 'scroll', 'align-items': 'center',  'justify-content': 'center',
            #       'display': 'flex', 'background-color': 'blue'}
        ),
        html.Br(),
        html.Div(
            dcc.Link(html.Button("Create again"), href="/", ),
            style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
        ),

    ]
)
