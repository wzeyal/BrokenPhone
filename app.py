import dash
from dash import dcc, html, dash_table
from controller import Controller
from model import Model

from dash.long_callback import DiskcacheLongCallbackManager

import diskcache

cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)

app = dash.Dash(__name__,
                long_callback_manager=long_callback_manager,
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

model = Model()
controller = Controller(app, model)

if __name__ == "__main__":
    app.run_server(debug=True)
