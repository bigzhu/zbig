#!/usr/bin/env python3

import logging
from zbig.zlog.logger import setup_logger, default_logger


class TestZLog:
    """Test suite for zlog module."""

    def test_setup_logger_default(self):
        """Test default logger setup."""
        logger = setup_logger("test_default")
        assert logger.name == "test_default"
        assert logger.level == logging.INFO

    def test_setup_logger_custom_level(self):
        """Test logger with custom level."""
        logger = setup_logger("test_debug", level="DEBUG")
        assert logger.level == logging.DEBUG

    def test_setup_logger_custom_format(self):
        """Test logger with custom format."""
        custom_format = "%(name)s - %(message)s"
        logger = setup_logger("test_format", format_string=custom_format)
        assert len(logger.handlers) > 0
        assert logger.handlers[0].formatter._fmt == custom_format

    def test_default_logger_exists(self):
        """Test that default logger is available."""
        assert default_logger is not None
        assert default_logger.name == "zbig"
