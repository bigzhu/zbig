#!/usr/bin/env python3

"""Logging utilities for zbig package."""

import logging
import sys
from typing import Optional


def create_configured_logger(
    logger_name: str = "zbig", log_level: str = "INFO", log_format: Optional[str] = None
) -> logging.Logger:
    """
    Create a logger with consistent formatting and configuration.

    Args:
        logger_name: Name for the logger instance
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_format: Custom format string for log messages

    Returns:
        Configured logger instance

    >>> logger = create_configured_logger("test")
    >>> logger.info("Test message")  # doctest: +SKIP
    """
    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logger_instance = logging.getLogger(logger_name)

    # Avoid adding handlers multiple times
    if not logger_instance.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        log_formatter = logging.Formatter(log_format)
        console_handler.setFormatter(log_formatter)
        logger_instance.addHandler(console_handler)

    logger_instance.setLevel(getattr(logging, log_level.upper()))
    return logger_instance


# Default logger instance
default_logger = create_configured_logger()

# Backward compatibility alias
setup_logger = create_configured_logger


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
