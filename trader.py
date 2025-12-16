import time
from telegram_bot import robo_ligado

def iniciar_trader():
    print("📈 Trader 24h iniciado")

    while True:
        if not robo_ligado():
            print("⏸️ Robô desligado — aguardando /on")
            time.sleep(5)
            continue

        # 🔽 AQUI entra sua lógica real
        print("💹 BTCUSDT preço atual:", obter_preco())  # exemplo

        time.sleep(60)
