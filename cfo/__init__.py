from logging.config import dictConfig
from typing import Literal

from flask import Flask

from .log_conf import d
from .models import db


def create_app(mode: Literal["dev", "test", "prod"]) -> Flask:
    server = Flask(__name__, instance_relative_config=True)

    # Configure logging
    dictConfig(d)

    # Modify server config settings
    if mode == "dev":
        server.config.from_object("config.DevelopmentConfig")
    elif mode == "test":
        server.config.from_object("config.TestConfig")
    elif mode == "prod":
        server.config.from_object("config.ProductionConfig")

    # Initalise db
    # db.init_app(server)

    with server.app_context():
        # Create tables
        # db.create_all()

        # Import Dash app
        from .init_dashboard_app import init_dashboard_app

        server = init_dashboard_app(server)

    # ==================================
    # DELETE
    # ==================================
    # testing
    @server.route("/abc")
    def hello():
        return "Hello World"

    return server
