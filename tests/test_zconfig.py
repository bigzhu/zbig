#!/usr/bin/env python3

import os
from unittest.mock import patch
from zbig.zconfig.settings import Settings


class TestZConfig:
    """Test suite for zconfig module."""

    def test_settings_default_values(self):
        """Test default configuration values."""
        settings = Settings()
        assert settings.log_level == "INFO"
        assert settings.cache_dir == os.path.expanduser("~/.zbig/cache")

    @patch.dict(os.environ, {"ZBIG_LOG_LEVEL": "DEBUG"})
    def test_settings_environment_override(self):
        """Test environment variable override."""
        settings = Settings()
        assert settings.log_level == "DEBUG"

    @patch.dict(os.environ, {
        "TELEGRAM_BOT_TOKEN": "test_token",
        "TELEGRAM_CHAT_ID": "test_chat_id"
    })
    def test_telegram_config_validation(self):
        """Test Telegram configuration validation."""
        settings = Settings()
        assert settings.validate_telegram_config() is True
        assert settings.telegram_bot_token == "test_token"
        assert settings.telegram_chat_id == "test_chat_id"

    def test_telegram_config_validation_missing(self):
        """Test validation with missing config."""
        settings = Settings()
        # Without environment variables, should be False
        assert settings.validate_telegram_config() is False