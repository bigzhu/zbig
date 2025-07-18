#!/usr/bin/env python3

"""Custom exceptions for zbig.ztelegram module."""


class TelegramError(Exception):
    """Base exception for Telegram-related errors."""

    pass


class TelegramConfigError(TelegramError):
    """Raised when Telegram configuration is missing or invalid."""

    pass


class TelegramSendError(TelegramError):
    """Raised when message/photo sending fails."""

    pass


class FileNotFoundError(TelegramError):
    """Raised when the specified file for photo sending doesn't exist."""

    pass
