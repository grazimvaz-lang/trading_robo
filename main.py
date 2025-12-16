import threading
import time
from telegram_bot import iniciar_bot
from trader import iniciar_trader

def main():
    print("🚀 Robô 24h iniciado (Telegram + Trader)")

    trader_thread = threading.Thread(
        target=iniciar_trader,
        daemon=False  # 🔴 IMPORTANTE: NÃO daemon
    )
    trader_thread.start()

    iniciar_bot()

    # mantém processo vivo caso o Telegram falhe
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
