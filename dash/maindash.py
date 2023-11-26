import dash
import dash_bootstrap_components as dbc

# my_app = dash.Dash("Dashapp", external_stylesheets=[dbc.themes.BOOTSTRAP])
my_app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
)
server = my_app.server
