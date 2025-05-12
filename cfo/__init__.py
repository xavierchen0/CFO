from typing import Literal
from flask import Flask
from .models import db
from .log_conf import d
from logging.config import dictConfig


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
    db.init_app(server)

    with server.app_context():
        # Create tables
        db.create_all()

        # Import Dash app
        from .dashboard import init_dashboard

        server = init_dashboard(server)

    # ==================================
    # DELETE
    # ==================================
    # testing
    @server.route("/")
    def hello():
        return "Hello World"

    return server
