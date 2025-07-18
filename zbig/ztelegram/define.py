import telebot
from environs import Env
import sys
import os

run_path = sys.path[0]
env = Env()
env.read_env(f"{run_path}/.env")  # read .env file, if it exists

# Use environment variables with fallback for CI/testing
TEL_TOKEN = env("TEL_TOKEN", default=os.getenv("TEL_TOKEN", "dummy_token_for_testing"))
CHAT_ID = env("CHAT_ID", default=os.getenv("CHAT_ID", "dummy_chat_id"))

bot = telebot.TeleBot(TEL_TOKEN, parse_mode=None)
