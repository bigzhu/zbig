#!/usr/bin/env python3

"""Configuration management for zbig package."""

import os
from typing import Optional
from environs import Env


class Settings:
    """Central configuration management."""
    
    def __init__(self):
        self.env = Env()
        self.env.read_env()  # Read .env file if exists
    
    @property
    def telegram_bot_token(self) -> Optional[str]:
        """Get Telegram bot token from environment."""
        return self.env.str("TELEGRAM_BOT_TOKEN", default=None)
    
    @property
    def telegram_chat_id(self) -> Optional[str]:
        """Get Telegram chat ID from environment."""
        return self.env.str("TELEGRAM_CHAT_ID", default=None)
    
    @property
    def cache_dir(self) -> str:
        """Get cache directory path."""
        return self.env.str("ZBIG_CACHE_DIR", default=os.path.expanduser("~/.zbig/cache"))
    
    @property
    def log_level(self) -> str:
        """Get logging level."""
        return self.env.str("ZBIG_LOG_LEVEL", default="INFO")
    
    def validate_telegram_config(self) -> bool:
        """Check if Telegram configuration is complete."""
        return bool(self.telegram_bot_token and self.telegram_chat_id)


# Global settings instance
settings = Settings()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)