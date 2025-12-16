from telegram_bot import iniciar_bot
from trader import iniciar_trader

if __name__ == "__main__":
    print("🚀 Robô 24h iniciado (Telegram + Trader)")

    # Inicia o trader (loop contínuo)
    iniciar_trader()

    # Inicia o bot do Telegram (polling)
    iniciar_bot()
