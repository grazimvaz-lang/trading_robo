import time
from config import settings
from broker.binance_broker import BinanceBroker
from strategies.rsi_safe_strategy import RSISafeStrategy

# Se existir trailing_stop.py, importa:
try:
    from risk.trailing_stop import TrailingStop
except:
    TrailingStop = None


class TradingEngine:
    def __init__(self):
        print("🔌 Iniciando Engine...")

        # === BROKER (Binance) ===
        self.broker = BinanceBroker(
            api_key=settings.BINANCE_API_KEY,
            api_secret=settings.BINANCE_API_SECRET,
            testnet=settings.BINANCE_TESTNET
        )

        # === Estratégia (RSI segura) ===
        self.strategy = RSISafeStrategy()

        # === Trailing stop (opcional) ===
        self.trailing = TrailingStop() if TrailingStop else None

        # Controle interno
        self.last_action = None
        self.position_price = None

    # -------------------------------------------------------------------------

    def run_once(self):
        """Executa um único ciclo do robô"""

        print("\n--- Novo ciclo ---")

        # === Obtém candles ===
        df = self.broker.get_klines(settings.SYMBOL, settings.TIMEFRAME)
        if df is None or len(df) == 0:
            print("❌ Erro ao buscar candles.")
            return

        # === Gera sinal ===
        signal = self.strategy.generate_signal(df)
        print(f"SINAL GERADO: {signal}")

        # === Tratamento dos sinais ===
        if signal == "BUY":
            self.execute_buy()

        elif signal == "SELL":
            self.execute_sell()

        else:
            print("⏸ Sem operação – aguardando melhor oportunidade.")

        # === Ajustar trailing stop, se houver ===
        if self.trailing and self.position_price:
            new_stop = self.trailing.update(self.position_price)
            if new_stop:
                print(f"🔒 Novo trailing stop ajustado: {new_stop}")

    # -------------------------------------------------------------------------

    def execute_buy(self):
        print("🟢 Executando compra...")

        qty = self.broker.get_position_size(settings.RISK_POSITION_SIZE)
        price = self.broker.buy_market(settings.SYMBOL, qty)

        if price:
            self.last_action = "BUY"
            self.position_price = price
            print(f"🟩 Compra realizada a {price}")
        else:
            print("❌ Falha na compra.")

    # -------------------------------------------------------------------------

    def execute_sell(self):
        print("🔴 Executando venda...")

        qty = self.broker.get_position_size(settings.RISK_POSITION_SIZE)
        price = self.broker.sell_market(settings.SYMBOL, qty)

        if price:
            self.last_action = "SELL"
            self.position_price = None
            print(f"🟥 Venda realizada a {price}")
        else:
            print("❌ Falha na venda.")


# -------------------------------------------------------------------------
# Modo standalone (opcional, para testes)
# -------------------------------------------------------------------------

if __name__ == "__main__":
    engine = TradingEngine()

    while True:
        engine.run_once()
        time.sleep(settings.ENGINE_LOOP_SECONDS)
