import threading
import time

from telegram_bot import iniciar_bot
from trader import iniciar_trader


def main():
    print("🚀 Robô 24h iniciado (Telegram + Trader)")

    # Inicia o trader em uma thread separada (loop contínuo)
    trader_thread = threading.Thread(target=iniciar_trader, daemon=True)
    trader_thread.start()

    # Inicia o bot do Telegram (loop próprio async)
    iniciar_bot()


if __name__ == "__main__":
    main()
