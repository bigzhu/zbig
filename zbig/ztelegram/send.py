#!/usr/bin/env python

import os
from zbig.ztime import cn_now
from zbig.ztelegram.define import bot, CHAT_ID
from zbig.ztelegram.exceptions import TelegramSendError, FileNotFoundError


def send_message(message: str) -> None:
    """
    Send a text message via Telegram bot.

    Args:
        message: The message text to send

    Raises:
        TelegramSendError: If sending the message fails

    >>> send_message("zbig send_message test")  # doctest: +SKIP
    """
    try:
        bot.send_message(chat_id=CHAT_ID, text=f"{cn_now()} {message}")
    except Exception as e:
        raise TelegramSendError(f"Failed to send message: {e}") from e


def send_photo(file_path: str, caption: str) -> None:
    """
    Send a photo via Telegram bot.

    Args:
        file_path: Path to the image file
        caption: Caption text for the photo

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        TelegramSendError: If sending the photo fails

    >>> send_photo('WechatIMG1021.jpg', 'test')  # doctest: +SKIP
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, "rb") as photo:
            bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=caption)
    except Exception as e:
        raise TelegramSendError(f"Failed to send photo: {e}") from e


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
