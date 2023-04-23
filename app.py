# import dash
# from craiyon import CraiyonV1
# from dash import html, no_update
# from dash.dependencies import Input, Output, State
#
# app = dash.Dash(__name__,
#                 use_pages=True,
#                 meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
#                 )
#
# server = app.server
#
# app.layout = html.Div(
#     style={'height': '100vh', 'display': 'flex', 'flex-direction': 'column'},
#     children=[
#         html.Div(
#             style={'height': '10%', 'background-color': 'lightgray', 'display': 'flex', 'align-items': 'center',
#                    'justify-content': 'center'},
#             children=[
#                 html.Div("Broken Phone", style={'fontSize': '5vh', 'textAlign': 'center', }),
#             ]
#         ),
#         html.Div(
#             style={'height': '90%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
#             # style={'height': '90%'},
#             children=[
#                 dash.page_container
#             ]
#         ),
#         html.Div(
#             [
#                 html.Div(
#                     id='model_prompt'
#                 ),
#                 html.Div(
#                     id='model_image'
#                 )
#             ],
#             id="model"
#         )
#     ]
# )
#
# @app.callback(
#     Output('model_prompt', 'children'),
#     Input('manager_prompt', 'n_submit'),
#     State('manager_prompt', 'value'),
# )
# def update_prompt(n_submit, prompt_value):
#     print('update_prompt')
#     return prompt_value
#
#
# @app.callback(
#     [Output('output-image', 'children')],
#     [Input('model_prompt', 'children')],
# )
# def on_model_change(model_state):
#     print(model_state)
#
#     return no_update
#
#
# # @app.callback(
# #     Output('output-image', 'children'),
# #     [
# #         Input('upload-image', 'contents'),
# #         Input('my-input', 'n_submit'),
# #         State('my-input', 'value')
# #     ]
# # )
# # def update_output(content, text_input, text_value):
# #     if content is not None:
# #         print('content')
# #         return html.Img(src=content, style={'height': '60vh'})
# #
# #     if text_value is not None:
# #         print('text_value')
# #
# #         # return html.Img(src=content, style={'height': '60vh'})
# #
# #         generator = CraiyonV1()  # Instantiates the api wrapper
# #         result = generator.generate(f"{text_value}")
# #         data = result.images[0]
# #
# #         img = html.Img(src=f'data:image/jpeg;base64,{data}', style={'height': '60vh'})
# #         return img
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
#
# # -----------------------------------

import dash
from dash import dcc
from dash import html

from dash.long_callback import DiskcacheLongCallbackManager

# Diskcache
import diskcache

from controller import Controller
from model import Model

cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)

app = dash.Dash(__name__, long_callback_manager=long_callback_manager)


class View:
    def __init__(self):
        self.layout = html.Div([
            html.Label("Enter some text:"),
            dcc.Input(id="text-input", type="text"),
            # html.Button(id="generate-button", n_clicks=0, children="Generate random text"),
            dcc.Upload(
                id='upload-image',
                children=html.Button('Upload Image'),
                # style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
            ),
            html.Br(),
            html.Label(id="text-label-1", children=""),
            html.Label(id="text-label-2", children=""),
            dcc.Loading(
                html.Div(
                    id='output-image',
                    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'height': '65vh',
                           'max-height': '65vh'}
                )
            ),
        ])


model = Model()
view = View()
controller = Controller(app, model, view)

app.layout = view.layout

if __name__ == '__main__':
    app.run_server(debug=True)
