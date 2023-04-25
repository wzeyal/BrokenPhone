import dash
import dash_bootstrap_components as dbc
import diskcache
from dash.long_callback import DiskcacheLongCallbackManager

from controller import Controller
from model import Model
from pages.template import TemplateView

cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)

app = dash.Dash(__name__,
                # external_stylesheets=[dbc.themes.SKETCHY],
                long_callback_manager=long_callback_manager,
                use_pages=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                )

server = app.server

app.layout = TemplateView().layout

model = Model()
controller = Controller(app, model)

if __name__ == "__main__":
    app.run_server(debug=True)
