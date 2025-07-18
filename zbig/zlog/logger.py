#!/usr/bin/env python3

"""Logging utilities for zbig package."""

import logging
import sys
from typing import Optional


def setup_logger(
    name: str = "zbig",
    level: str = "INFO",
    format_string: Optional[str] = None
) -> logging.Logger:
    """
    Setup a logger with consistent formatting.
    
    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format_string: Custom format string
        
    Returns:
        Configured logger instance
        
    >>> logger = setup_logger("test")
    >>> logger.info("Test message")  # doctest: +SKIP
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    logger = logging.getLogger(name)
    
    # Avoid adding handlers multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(format_string)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    logger.setLevel(getattr(logging, level.upper()))
    return logger


# Default logger instance
default_logger = setup_logger()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)