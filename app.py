import dash
from craiyon import CraiyonV1
from dash import html
from dash.dependencies import Input, Output, State

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
    ]
)


@app.callback(
    Output('output-image', 'children'),
    [
        Input('upload-image', 'contents'),
        Input('my-input', 'n_submit'),
        State('my-input', 'value')
    ]
)
def update_output(content, text_input, text_value):

    if content is not None:
        print('content')
        return html.Img(src=content, style={'height': '60vh'})

    if text_value is not None:
        print('text_value')

        # return html.Img(src=content, style={'height': '60vh'})

        generator = CraiyonV1()  # Instantiates the api wrapper
        result = generator.generate(f"{text_value}")
        data = result.images[0]

        img = html.Img(src=f'data:image/jpeg;base64,{data}', style={'height': '60vh'})
        return img


if __name__ == "__main__":
    app.run_server(debug=True)
