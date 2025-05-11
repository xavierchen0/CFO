from cfo.models import db
from flask import Flask
from dash import Dash, html, clientside_callback, Input, Output
import dash_bootstrap_components as dbc
from .static.layout import layout


def init_dashboard(app) -> Flask:
    """
    Create a Plotly Dash dashboard
    """
    dashApp = Dash(
        server=app,
        routes_pathname_prefix="/dashboard/",
        external_stylesheets=[dbc.themes.DARKLY, dbc.icons.FONT_AWESOME],
    )
    create_callbacks(dashApp)

    dashApp.layout = layout

    return dashApp.server


def create_callbacks(dashApp: Dash) -> None:
    """
    Initialise callbacks
    """
