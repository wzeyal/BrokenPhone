import dash
from dash import dcc, html


class TemplateView:
    def __init__(self):
        self.layout = html.Div(
            [
                html.Div("My Phone", id="page_title"),
                html.Div(
                    dash.page_container,
                    id="page_body",
                ),

                # html.Div("Body", style={'background-color': 'blue'}, id="body"),

                # not rendered, just for routing
                dcc.Location(id='url', refresh=False),
                html.Div(id="hidden_div_for_redirect_callback"),
            ],
            className="template_view",
        )

    # html.Div(
    #     style={'height': '100vh', 'display': 'flex', 'flex-direction': 'column'},
    #     children=[
    #
    #         dcc.Location(id='url', refresh=False),
    #         html.Div(id="hidden_div_for_redirect_callback"),
    #
    #         html.Div(
    #             style={'height': '10%', 'background-color': 'lightgray', 'display': 'flex', 'align-items': 'center',
    #                    'justify-content': 'center'},
    #             children=[
    #                 html.Div("Broken Phone", style={'fontSize': '5vh', 'textAlign': 'center', }),
    #             ]
    #         ),
    #         html.Div(
    #             style={'height': '80%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
    #             # style={'height': '90%'},
    #             children=[
    #                 dash.page_container
    #             ]
    #         ),
    #         html.Div(
    #             style={'height': '10%'},
    #         )
    #     ]
    # )
