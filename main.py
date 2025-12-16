import threading
import time
from config import validate_config
from telegram_bot import iniciar_bot
from trader import executar_trader

def run_thread(func, name):
    t = threading.Thread(target=func, name=name, daemon=True)
    t.start()
    return t

if __name__ == "__main__":
    missing = validate_config()
    if missing:
        print("❌ Variáveis faltando:", ", ".join(missing))
        print("➡️ Verifique o arquivo .env")
        raise SystemExit(1)

    print("🚀 Robô 24h iniciado (Telegram + Trader)")

    run_thread(iniciar_bot, "telegram")
    run_thread(executar_trader, "trader")

    # mantém o processo vivo
    while True:
        time.sleep(60)
