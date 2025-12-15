import pandas as pd
import ta

from strategies.base_strategy import BaseStrategy


class RSISafeStrategy(BaseStrategy):
    """
    Estratégia segura baseada em RSI com filtro de tendência.
    Compra somente em zonas muito seguras e vende somente em forte sobrecompra.
    """

    def __init__(self, rsi_buy=25, rsi_sell=75, trend_period=50):
        self.rsi_buy = rsi_buy
        self.rsi_sell = rsi_sell
        self.trend_period = trend_period

    def generate_signal(self, df: pd.DataFrame) -> str:
        df = df.copy()

        # Calcula o RSI
        df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()

        # Média móvel para confirmar direção da tendência
        df["ma"] = df["close"].rolling(self.trend_period).mean()

        last = df.iloc[-1]
        rsi = last["rsi"]
        price = last["close"]

        # Se o preço está acima da média → tendência de alta
        uptrend = price > last["ma"]

        # COMPRA SEGURA
        if rsi < self.rsi_buy and uptrend:
            return "buy"

        # VENDA SEGURA
        if rsi > self.rsi_sell and not uptrend:
            return "sell"

        return "hold"
