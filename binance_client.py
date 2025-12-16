from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def get_price(symbol: str):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])
