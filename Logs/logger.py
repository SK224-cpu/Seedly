import logging
import sys
from pythonjsonlogger import jsonlogger
import os


def get_logger(name="app", level=logging.INFO, log_file_path="Logs/app.log"):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  # Prevent adding duplicate handlers

    logger.setLevel(level)

    # JSON formatter for structured logs
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(levelname)s %(name)s %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Ensure log directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # File handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

