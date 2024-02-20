from time_z.now import now
from .define import bot, CHAT_ID


def send_message(message: str):
    bot.send_message(chat_id=CHAT_ID, text=f"{now()} {message}")


if __name__ == "__main__":
    send_message('bigzhu_py send_message test')
