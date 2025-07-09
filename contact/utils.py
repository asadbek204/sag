from config.settings import BOT_ID, TELEGRAM_API_URL, CHAT_ID
import requests

def send_message_telegram(message):
    return requests.get(TELEGRAM_API_URL.format(BOT_ID, message, CHAT_ID))