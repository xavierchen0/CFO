from typing import Literal
from flask import Flask
from .models import db
from .log_conf import d
from logging.config import dictConfig


def create_app(mode: Literal["dev", "test", "prod"]) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    # Configure logging
    dictConfig(d)

    # Modify app config settings
    if mode == "dev":
        app.config.from_object("config.DevelopmentConfig")
    elif mode == "test":
        app.config.from_object("config.TestConfig")
    elif mode == "prod":
        app.config.from_object("config.ProductionConfig")

    # Initalise db
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

        # Import Dash app
        from .dashboard import init_dashboard

        app = init_dashboard(app)

    # ==================================
    # DELETE
    # ==================================
    # testing
    @app.route("/")
    def hello():
        return "Hello World"

    return app
