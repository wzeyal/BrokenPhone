import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


dash.register_page(__name__)


class FinalView:
    def __init__(self):
        self.layout = html.Div(
            style={'align-items': 'center', 'justify-content': 'center'},
            # 'display': 'flex', 'flex-direction': 'column'
            children=[
                html.Div("test"),
                dbc.Carousel(
                    items=[
                    {"key": "1", "src": "https://via.placeholder.com/150x15"}
                    ],
                    controls=True,
                    indicators=True
                ),
                # html.Div(
                #     [
                #         html.Img(src='https://via.placeholder.com/150x150', id="1"),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #         # html.Img(src='https://via.placeholder.com/150x150'),
                #     ],
                #     className='centered-div',
                #     style={'height': '70vh', 'overflow-y': 'auto', },
                #
                #     # style={'height': '70vh', 'overflow-y': 'scroll', 'align-items': 'center',  'justify-content': 'center',
                #     #       'display': 'flex', 'background-color': 'blue'}
                # ),
                # html.Br(),
                dcc.Link(html.Button("Create Again"), href="/", ),
                html.Div(

                    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
                ),

            ]
        )


layout = FinalView().layout
