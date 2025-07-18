#!/usr/bin/env python3

"""Configuration management for zbig package."""

import os
from typing import Optional
from environs import Env


class ApplicationSettings:
    """Central configuration management for the application."""

    def __init__(self):
        self.environment_parser = Env()
        self.environment_parser.read_env()  # Read .env file if exists

    @property
    def telegram_bot_token(self) -> Optional[str]:
        """Get Telegram bot token from environment variables."""
        return self.environment_parser.str("TELEGRAM_BOT_TOKEN", default=None)

    @property
    def telegram_chat_id(self) -> Optional[str]:
        """Get Telegram chat ID from environment variables."""
        return self.environment_parser.str("TELEGRAM_CHAT_ID", default=None)

    @property
    def cache_directory_path(self) -> str:
        """Get cache directory path from environment or default."""
        return self.environment_parser.str(
            "ZBIG_CACHE_DIR", default=os.path.expanduser("~/.zbig/cache")
        )

    @property
    def logging_level(self) -> str:
        """Get logging level from environment or default."""
        return self.environment_parser.str("ZBIG_LOG_LEVEL", default="INFO")

    def is_telegram_configuration_complete(self) -> bool:
        """Check if Telegram configuration is complete and valid."""
        return bool(self.telegram_bot_token and self.telegram_chat_id)


# Global settings instance
application_settings = ApplicationSettings()

# Backward compatibility alias
settings = application_settings


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
