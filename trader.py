import time
from state import status
from binance_client import get_price

SYMBOL = "BTCUSDT"
SLEEP_SECONDS = 30  # segundos entre ciclos

def executar_trader():
    print("📈 Trader 24h iniciado")

    while True:
        try:
            if status():
                price = get_price(SYMBOL)
                print(f"🔍 {SYMBOL} preço atual: {price}")
            else:
                print("⏸️ Robô desligado (aguardando /on)")

            time.sleep(SLEEP_SECONDS)

        except Exception as e:
            print(f"❌ Erro no trader: {e}")
            time.sleep(10)
