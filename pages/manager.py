import dash
from dash import dcc, html

dash.register_page(__name__)

nof_players = 5
game_pin = 123456

# layout = html.Div(
#     [
#         dcc.Markdown(f'# {game_pin}'),
#         dcc.Markdown(f'# Number of players: {nof_players}'),
#         dcc.Input(placeholder="Describe in details"),
#         html.Button('Submit', id='submit-val', n_clicks=0),
#         html.Button('Or upload an image', id='upload', n_clicks=0),
#         dcc.Upload(
#                 id='upload-data',
#                 children=html.Div([
#                     'Drag and Drop or ',
#                     html.A('Select Files')
#                 ]),
#                 style={
#                     'width': '100%',
#                     'height': '60px',
#                     'lineHeight': '60px',
#                     'borderWidth': '1px',
#                     'borderStyle': 'dashed',
#                     'borderRadius': '5px',
#                     'textAlign': 'center',
#                     'margin': '10px'
#                 },
#                 # Allow multiple files to be uploaded
#                 multiple=True
#             ),
#         html.Div(id='output-data-upload'),
#         dcc.Link(html.Button("Start Game"), href="/final",)
#
#     ]
# )

layout = html.Div(

    # style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
    style={'display': 'flex', 'flex-direction': 'column'},

    children=[
        dcc.Upload(
                id='upload-image',
                children=html.Button('Upload Image')
            ),
        html.Div(id='output-image'),
        dcc.Link(html.Button("Start Game"), href="/final",)
    ]
)
