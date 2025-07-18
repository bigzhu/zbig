#!/usr/bin/env python

import os
from zbig.ztime import get_china_current_time
from zbig.ztelegram.define import telegram_bot as bot, TELEGRAM_CHAT_ID as CHAT_ID
from zbig.ztelegram.exceptions import TelegramSendError, FileNotFoundError


def send_text_message(message_text: str) -> None:
    """
    Send a text message via Telegram bot with timestamp.

    Args:
        message_text: The message content to send

    Raises:
        TelegramSendError: If sending the message fails

    >>> send_text_message("zbig send_message test")  # doctest: +SKIP
    """
    try:
        timestamped_message = f"{get_china_current_time()} {message_text}"
        bot.send_message(chat_id=CHAT_ID, text=timestamped_message)
    except Exception as telegram_error:
        raise TelegramSendError(
            f"Failed to send message: {telegram_error}"
        ) from telegram_error


def send_photo_message(image_path: str, photo_caption: str) -> None:
    """
    Send a photo via Telegram bot with caption.

    Args:
        image_path: Path to the image file
        photo_caption: Caption text for the photo

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        TelegramSendError: If sending the photo fails

    >>> send_photo_message('WechatIMG1021.jpg', 'test')  # doctest: +SKIP
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        with open(image_path, "rb") as photo_file:
            bot.send_photo(chat_id=CHAT_ID, photo=photo_file, caption=photo_caption)
    except Exception as telegram_error:
        raise TelegramSendError(
            f"Failed to send photo: {telegram_error}"
        ) from telegram_error


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
