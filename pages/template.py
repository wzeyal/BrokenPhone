import dash
import dash_bootstrap_components as dbc
from dash import dcc, html


class AppView:
    def __init__(self):
        self.layout = dbc.Container([

            dbc.Row(
                dbc.Col(
                    html.H1("Broken Phone"),
                    width={'size': 6, 'offset': 3},
                    style={'text-align': 'center'}
                ),
            ),
            # dbc.NavbarSimple(
            #     brand="AI Phone Home", className='no-gutters', color='primary', dark=True,),
            dash.page_container,
            dcc.Location(id='url', refresh=False),
            html.Div(id="hidden_div_for_redirect_callback"),

        ],
            style={
                # Apply landscape styles when screen width is greater than height
                '@media (min-aspect-ratio: 1/1)': {
                    'height': '100vh',
                    'max-height': '100vw',
                    'overflow-x': 'hidden'
                }
            }
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
