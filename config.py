from os import getenv
from typing import ClassVar

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Base config
    """

    TESTING: bool = False
    SECRET_KEY: ClassVar[str | None] = getenv("SECRET_KEY")


class DevelopmentConfig(Config):
    """
    Development config
    """

    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


class TestConfig(Config):
    """
    Test config
    """

    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test-project.db"


class ProductionConfig(Config):
    """
    Production config
    """
