import dash
from dash import dcc, html

dash.register_page(__name__, path='/')

# layout = html.Div(
#     [
#         # dcc.Markdown(f'# {__name__}'),
#         dcc.Link(html.Button("Create Game"), href="/manager",)
#     ]
# )

layout = html.Div(
    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
    children=[
        dcc.Link(html.Button("Create Game3"), href="/managerr",)
    ]
)
#              # style={'height': '90%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},

# dcc.Upload(
#         id='upload-image',
#         children=html.Button('Upload Image')
#     ),
#     html.Div(id='output-image')
