from craiyon import CraiyonV1
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
import random

class Controller:
    def __init__(self, app, model, view):
        self.app = app
        self.model = model
        self.view = view

        self.register_callbacks()

    def register_callbacks(self):
        @self.app.long_callback(
            Output("output-image", "children", allow_duplicate=True),
            [Input("text-input", "n_submit")],
            State("text-input", "value"),
            running=[
                (Output("upload-image", "disabled"), True, False),
            ],
            prevent_initial_call=True
        )
        def update_text_label(n_submit, text):
            self.model.update_text(text)
            generator = CraiyonV1()  # Instantiates the api wrapper
            result = generator.generate(f"{text}")
            data = result.images[0]

            return html.Img(src=f'data:image/jpeg;base64,{data}', style={'height': '60vh'})

        @self.app.callback(
            Output("output-image", "children"),
            [Input('upload-image', 'contents'), ],

        )
        def on_upload_image(content):
            self.model.update_image(content)
            return html.Img(src=content, style={'height': '60vh'})
            # self.model.generate_text()
            # return self.model.text