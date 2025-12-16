import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")

def validate_config():
    missing = []
    if not BINANCE_API_KEY:
        missing.append("BINANCE_API_KEY")
    if not BINANCE_API_SECRET:
        missing.append("BINANCE_API_SECRET")
    if not TELEGRAM_TOKEN:
        missing.append("TELEGRAM_TOKEN")
    return missing
