import dash
import dash_bootstrap_components as dbc
from dash import Dash
from flask import Flask

from cfo.static.dashboard_layout import dashboard_layout
from cfo.static.upload_files_layout import upload_files_layout


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

    # Register Dashboard and Upload Files Page

    dash.register_page("dashboard", path="/", layout=dashboard_layout)
    dash.register_page(
        "upload files", path="/upload", layout=upload_files_layout
    )

    # Initialise callbacks
    create_callbacks(dash_app)

    return dash_app.server


def create_callbacks(dash_app: Dash) -> None:
    """
    Initialise callbacks
    """
