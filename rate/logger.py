import logging


def logger() -> logging.Logger:
    """Represent logger for console."""

    log = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt='%(asctime)s     %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    return log
