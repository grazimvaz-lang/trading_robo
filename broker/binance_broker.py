from binance.client import Client
from binance.enums import *
import pandas as pd
import time


class BinanceBroker:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = False):
        """Inicializa o broker da Binance."""
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet

        if testnet:
            self.client = Client(api_key, api_secret, testnet=True)
            self.client.API_URL = 'https://testnet.binance.vision/api'
        else:
            self.client = Client(api_key, api_secret)

    # =========================================
    # PREÇO ATUAL
    # =========================================
    def get_price(self, symbol: str) -> float:
        """Retorna o preço atual do ativo."""
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            return float(ticker["price"])
        except Exception as e:
            print("Erro ao buscar preço:", e)
            return None

    # =========================================
    # HISTÓRICO DE CANDLES
    # =========================================
    def get_klines(self, symbol: str, interval: str, limit: int = 100):
        """Retorna candles em formato DataFrame."""
        try:
            raw = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
            df = pd.DataFrame(raw, columns=[
                "open_time", "open", "high", "low", "close", "volume",
                "close_time", "qav", "num_trades", "taker_base_vol",
                "taker_quote_vol", "ignore"
            ])

            df["open"] = pd.to_numeric(df["open"])
            df["high"] = pd.to_numeric(df["high"])
            df["low"] = pd.to_numeric(df["low"])
            df["close"] = pd.to_numeric(df["close"])
            df["volume"] = pd.to_numeric(df["volume"])

            return df

        except Exception as e:
            print("Erro ao obter candles:", e)
            return None

    # =========================================
    # SALDO DA CONTA
    # =========================================
    def get_balance(self, asset="USDT") -> float:
        """Retorna o saldo disponível."""
        try:
            info = self.client.get_asset_balance(asset=asset)
            return float(info["free"])
        except Exception as e:
            print("Erro ao pegar saldo:", e)
            return 0.0

    # =========================================
    # ORDEM DE COMPRA
    # =========================================
    def buy_market(self, symbol: str, quantity: float):
        """Executa compra a mercado."""
        try:
            order = self.client.order_market_buy(
                symbol=symbol,
                quantity=quantity
            )
            return order
        except Exception as e:
            print("Erro ao comprar:", e)
            return None

    # =========================================
    # ORDEM DE VENDA
    # =========================================
    def sell_market(self, symbol: str, quantity: float):
        """Executa venda a mercado."""
        try:
            order = self.client.order_market_sell(
                symbol=symbol,
                quantity=quantity
            )
            return order
        except Exception as e:
            print("Erro ao vender:", e)
            return None


# ============================================================
# TESTE MANUAL AO RODAR O ARQUIVO DIRETAMENTE
# ============================================================
if __name__ == "__main__":
    from config.settings import BINANCE_API_KEY, BINANCE_API_SECRET, BINANCE_TESTNET

    print("🔌 Testando conexão com a Binance...")

    broker = BinanceBroker(
        api_key=BINANCE_API_KEY,
        api_secret=BINANCE_API_SECRET,
        testnet=BINANCE_TESTNET
    )

    try:
        balance = broker.get_balance()
        print(f"💰 Saldo disponível: {balance} USDT")

        price = broker.get_price("BTCUSDT")
        print(f"📈 Preço atual do BTCUSDT: {price}")

        print("✔ Conexão funcionando corretamente!")
    except Exception as e:
        print("❌ Erro ao testar a Binance:")
        print(e)
