import dash
from dash import html, dcc
import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
from craiyon import CraiyonV1

# from PIL import Image
from io import BytesIO
import base64


import pandas as pd

# app = dash.Dash(__name__, use_pages=True)

app = dash.Dash(__name__,
                use_pages=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                )

server = app.server

app.layout = html.Div(
    style={'height': '100vh', 'display': 'flex', 'flex-direction': 'column'},
    children=[
        html.Div(
            style={'height': '10%', 'background-color': 'lightgray', 'display': 'flex', 'align-items': 'center',
                   'justify-content': 'center'},
            children=[
                html.Div("Broken Phone", style={'fontSize': '5vh', 'textAlign': 'center', }),
            ]
        ),
        html.Div(
            style={'height': '90%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
            # style={'height': '90%'},
            children=[
                dash.page_container
            ]
        )
        # dash.page_container
    ]
)
#
#
# def parse_contents(contents, filename, date):
#     content_type, content_string = contents.split(',')
#
#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             # Assume that the user uploaded a CSV file
#             df = pd.read_csv(
#                 io.StringIO(decoded.decode('utf-8')))
#         elif 'xls' in filename:
#             # Assume that the user uploaded an excel file
#             df = pd.read_excel(io.BytesIO(decoded))
#     except Exception as e:
#         print(e)
#         return html.Div([
#             'There was an error processing this file.'
#         ])
#
#     return html.Div([
#         html.H5(filename),
#         html.H6(datetime.datetime.fromtimestamp(date)),
#
#         dash_table.DataTable(
#             df.to_dict('records'),
#             [{'name': i, 'id': i} for i in df.columns]
#         ),
#
#         html.Hr(),  # horizontal line
#
#         # For debugging, display the raw contents provided by the web browser
#         html.Div('Raw Content'),
#         html.Pre(contents[0:200] + '...', style={
#             'whiteSpace': 'pre-wrap',
#             'wordBreak': 'break-all'
#         })
#     ])
#
#
# @app.callback(Output('output-data-upload', 'children'),
#               Input('upload-data', 'contents'),
#               State('upload-data', 'filename'),
#               State('upload-data', 'last_modified'))
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children
#
#

@app.callback(Output('output-image', 'children'),
              [Input('upload-image', 'contents')])
def update_output(content):
    # generator = CraiyonV1()  # Instantiates the api wrapper
    # result = generator.generate("Photorealistic image of shrek eating earth")
    # decoded = BytesIO(base64.b64decode(result.images[1]))
    # return html.Img(src=decoded, style={'max-width': '100%'})

    if content is not None:
        generator = CraiyonV1() # Instantiates the api wrapper
        result = generator.generate("Photorealistic image of shrek eating earth")
        from PIL import Image
        data = result.images[0]
        # data = base64.b64decode(data)
        # data = BytesIO(data)

        img = html.Img(src=f'data:image/jpeg;base64,{data}')
        return img

        im = Image.open(BytesIO(base64.b64decode(result.images[0])))

        data = content.split(',')[1]
        # img = html.Img(src=f'data:image/jpeg;base64,{data}', style={'width': '100%'})
        img = html.Img(src=f'data:image/jpeg;base64,{data}', style={'width': '100%'})
        return img

        # Decode the base64-encoded image
        _, content_string = content.split(',')
        decoded = base64.b64decode(content_string)
        # Convert the image to a BytesIO object
        image = io.BytesIO(decoded)
        # Display the image
        img = html.Img(src=f'data:image/jpeg;base64,{image}', style={'width': '100%'})
        return img
        return html.Img(src=content, style={'max-width': '100%'})


if __name__ == "__main__":
    app.run_server(debug=True)

# import dash
# import dash_html_components as html
# import dash_core_components as dcc
# from dash.dependencies import Input, Output, State
#
# app = dash.Dash()
#
# app.layout = html.Div(
#     style={'height': '100vh', 'display': 'flex', 'flex-direction': 'column'},
#     children=[
#         html.Div(
#             style={'height': '10%', 'background-color': 'lightgray', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
#             children=[
#                 html.H1('Broken Phone')
#             ]
#         ),
#         html.Div(
#             id='main-screen',
#             style={'height': '90%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
#             children=[
#                 html.Button('Create Game', id='create-game-button', n_clicks=0)
#             ]
#         ),
#         html.Div(
#             id='manage-screen',
#             style={'height': '90%', 'display': 'none', 'align-items': 'center', 'justify-content': 'center'},
#             children=[
#                 dcc.Upload(
#                     id='upload-image',
#                     children=html.Button('Upload Image'),
#                     accept='image/*'
#                 ),
#                 html.Br(),
#                 html.Img(id='image-preview', style={'max-width': '100%'}),
#                 html.Br(),
#                 html.Button('Go to Final Screen', id='final-screen-button', n_clicks=0)
#             ]
#         ),
#         html.Div(
#             id='final-screen',
#             style={'height': '90%', 'display': 'none', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'center'},
#             children=[
#                 html.Div(id='image-gallery', style={'width': '50%'}),
#                 html.Br(),
#                 html.Button('Return to Main Screen', id='return-to-main-button', n_clicks=0)
#             ]
#         )
#     ]
# )
#
# @app.callback(Output('manage-screen', 'style'),
#               [Input('create-game-button', 'n_clicks')])
# def show_manage_screen(n_clicks):
#     if n_clicks > 0:
#         return {'height': '90%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
#     else:
#         return {'height': '90%', 'display': 'none', 'align-items': 'center', 'justify-content': 'center'}
#
# @app.callback(Output('final-screen', 'style'),
#               [Input('final-screen-button', 'n_clicks')])
# def show_final_screen(n_clicks):
#     if n_clicks > 0:
#         return {'height': '90%', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'center'}
#     else:
#         return {'height': '90%', 'display': 'none', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'center'}
#
# @app.callback(Output('image-preview', 'src'),
#               [Input('upload-image', 'contents')])
# def update_image_preview(contents):
#     if contents is not None:
#         return contents
#
# @app.callback(Output('image-gallery', 'children'),
#               [Input('upload-image', 'contents')])
# def update_image_gallery(contents):
#     if contents is not None:
#         return html.Img(src=contents, style={'max-width': '100%'})
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
