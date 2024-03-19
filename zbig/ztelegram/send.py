#!/usr/bin/env python


from zbig.ztime import cn_now
from zbig.ztelegram.define import bot, CHAT_ID


def send_message(message: str):
    """

    Args:
        message:

    >>> send_message("zbig send_message test")
    """
    bot.send_message(chat_id=CHAT_ID, text=f"{cn_now()} {message}")


def send_photo(file_path: str, caption: str):
    """

    Args:
        file_path:
        caption:

    >>> send_photo('WechatIMG1021.jpg', 'test')
    """
    photo = open(file_path, "rb")
    bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=caption)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
