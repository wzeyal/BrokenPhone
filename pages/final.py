import dash
from dash import dcc, html

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