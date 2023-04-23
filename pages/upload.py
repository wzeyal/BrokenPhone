import dash
from dash import dcc, html

dash.register_page(__name__)


class UploadView:
    def __init__(self):
        self.layout = html.Div(

            # style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
            style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center', 'align-items': 'center'},

            children=[

                html.Div(
                    [
                        # html.Button(
                        #     "text",
                        #     id='generate-picture'
                        # ),
                        dcc.Input(id='manager_prompt', type='text', placeholder='Enter text here ...'),

                        html.Button("Create Image", id="create"),


                    ],
                    style={'display': 'flex', 'gap': '5px'}
                ),

                html.Br(),

                dcc.Upload(
                    id='upload-image',
                    children=html.Button('Upload Image'),
                    # style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
                ),

                dcc.Loading(
                    html.Div(
                        id='output-image',
                        style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center',
                               'height': '65vh',
                               'max-height': '65vh'}
                    ),
                ),

                dcc.Link(html.Button("Start Game", id="start-game", disabled=True), href="/final", )
            ]
        )


layout = UploadView().layout
