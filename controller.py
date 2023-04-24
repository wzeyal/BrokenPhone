from craiyon import CraiyonV1
from dash.dependencies import Input, Output, State
from dash import html, no_update, dcc


# from furl import furl

class Controller:
    def __init__(self, app, model):
        self.app = app
        self.model = model

        self.register_callbacks()

    def register_callbacks(self):
        @self.app.long_callback(
            Output("output-image", "children", allow_duplicate=True),
            [Input("create", "n_clicks")],
            State("manager_prompt", "value"),
            running=[
                (Output("upload-image", "disabled"), True, False),
                (Output("create", "disabled"), True, False),
                (Output("start-game", "disabled"), True, False),
            ],
            prevent_initial_call=True
        )
        def update_text_label(n_submit, text):
            self.model.update_text(text)
            generator = CraiyonV1()  # Instantiates the api wrapper
            result = generator.generate(f"{text}")
            data = result.images[0]

            return html.Img(src=f'data:image/jpeg;base64,{data}', style={'height': '60vh'})

        @self.app.long_callback(
            Output("output-image", "children", allow_duplicate=True),
            [Input('upload-image', 'contents'), ],
            prevent_initial_call=True,
            running=[
                (Output("upload-image", "disabled"), True, False),
                (Output("create", "disabled"), True, False),
                (Output("start-game", "disabled"), True, False),
            ],

        )
        def on_upload_image(content):
            self.model.update_image(content)
            return html.Img(src=content, style={'height': '60vh'})

        @self.app.callback(Output('hidden_div_for_redirect_callback', 'children'),
                      [Input('url', 'href')])
        def _content(href: str):
            if "goto" in href:
                return dcc.Location(pathname="/final", id="someid_doesnt_matter")
            return  no_update
            raise PreventUpdate()
            print(href)

            if "12" in href:
                return "final"
            print(href)
            return "final"
            return no_update
            # f = furl(href)
            # param1 = f.args['param1']
            # param2 = f.args['param2']
