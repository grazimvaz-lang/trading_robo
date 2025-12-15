import pandas as pd
import ta

from strategies.base_strategy import BaseStrategy


class RSIStrategy(BaseStrategy):
    def __init__(self, rsi_buy: int = 30, rsi_sell: int = 70):
        self.rsi_buy = rsi_buy
        self.rsi_sell = rsi_sell

    def generate_signal(self, df: pd.DataFrame) -> str:
        df = df.copy()

        df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
        last_rsi = df["rsi"].iloc[-1]

        print(f"RSI atual: {last_rsi:.2f}")

        if last_rsi < self.rsi_buy:
            return "buy"

        if last_rsi > self.rsi_sell:
            return "sell"

        return "hold"
