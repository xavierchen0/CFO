"""
Logging Configurations

Example Usage:
```python
import logging
from logging_conf import CustomFormatter

# Initialise logger
logger = logging.getLogger()
# Initialise handler to read and write logs
handler = logging.StreamHandler()
# Set handler's Formatter
handler.setFormatter(CustomFormatter())
# Add handler to logger
logger.addHandler(handler)
# (Optional) set lowest log level as DEBUG
logger.setLevel(logging.DEBUG)
```
"""

import logging


class CustomFormatter(logging.Formatter):
    # Color RGB
    bolddarkred = "\x1b[1;38;2;235;111;146m"
    red = "\x1b[38;2;240;154;160m"
    yellow = "\x1b[38;2;246;193;119m"
    green = "\x1b[38;2;119;221;119m"
    cyan = "\x1b[38;2;183;255;250m"
    reset = "\x1b[0m"

    # Emojis
    # Don't change the whitespaces; it is to make sure formatting is good
    debug_icon = "[\U0001f41e "
    info_icon = "[\u2139 "
    warning_icon = "[\u26a0 "
    error_icon = "[\u274c "
    critical_icon = "[\U0001f525 "

    # Displayed format
    format = "%(levelname)s] [%(asctime)s] [%(filename)s:%(funcName)s]:"
    message = "    %(message)s"

    # Formats
    FORMATS = {
        logging.DEBUG: cyan + debug_icon + format + reset + message,
        logging.INFO: green + info_icon + format + reset + message,
        logging.WARNING: yellow + warning_icon + format + reset + message,
        logging.ERROR: red + error_icon + format + reset + message,
        logging.CRITICAL: bolddarkred
        + critical_icon
        + format
        + reset
        + message,
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
