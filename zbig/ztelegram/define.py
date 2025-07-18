import telebot
from environs import Env
import sys
import os

# Get current script directory for .env file
script_directory = sys.path[0]
env_parser = Env()
env_parser.read_env(f"{script_directory}/.env")  # read .env file, if it exists

# Use environment variables with fallback for CI/testing
TELEGRAM_BOT_TOKEN = env_parser(
    "TEL_TOKEN", default=os.getenv("TEL_TOKEN", "dummy_token_for_testing")
)
TELEGRAM_CHAT_ID = env_parser("CHAT_ID", default=os.getenv("CHAT_ID", "dummy_chat_id"))

# Initialize Telegram bot instance
telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)
