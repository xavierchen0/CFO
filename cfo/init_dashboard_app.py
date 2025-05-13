import dash
import dash_bootstrap_components as dbc
from dash import Dash, html
from flask import Flask

from cfo.static.dashboard_layout import dashboard_layout


def init_dashboard_app(server) -> Flask:
    """
    Create a Plotly Dash dashboard
    """
    # Create Dash app
    dash_app = Dash(
        server=server,
        routes_pathname_prefix="/dashboard/",
        external_stylesheets=[dbc.themes.DARKLY, dbc.icons.FONT_AWESOME],
        use_pages=True,
        pages_folder="",
    )

    # Initialise callbacks
    create_callbacks(dash_app)

    return dash_app.server


def create_callbacks(dashApp: Dash) -> None:
    """
    Initialise callbacks
    """
