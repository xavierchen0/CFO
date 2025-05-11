"""
Logging configurations
"""

import logging


class CustomFormatter(logging.Formatter):
    # Color RGB
    bolddarkred = "\x1b[1;38;2;235;111;146m"
    red = "\x1b[38;2;240;154;160m"
    yellow = "\x1b[38;2;246;193;119m"
    green = "\x1b[38;2;119;221;119m"
    cyan = "\x1b[38;2;183;255;250m"

    # Displayed format
    format = "%(asctime)s [%(levelname)s]: %(filename)s:%(funcName)s - %(message)s"

    # Formats
    FORMATS = {
        logging.DEBUG: cyan + format,
        logging.INFO: green + format,
        logging.WARNING: yellow + format,
        logging.ERROR: red + format,
        logging.CRITICAL: bolddarkred + format,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


d = {
    "version": 1,
    "formatters": {"custom": {"()": "cfo.log_conf.CustomFormatter"}},
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "custom",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["wsgi"]},
}
