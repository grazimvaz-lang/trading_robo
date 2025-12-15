import time

print("⚙️ Engine iniciando...")

# ===============================
# Tentativa segura de importar Binance
# ===============================
try:
    from broker.binance_broker import BinanceBroker
    print("✅ BinanceBroker carregado com sucesso")
except Exception as e:
    print("⚠️ Binance desativado temporariamente:", e)
    BinanceBroker = None


def start_engine():
    print("🚀 Engine iniciado")

    if BinanceBroker is None:
        print("ℹ️ Rodando sem Binance (modo seguro)")
    else:
        print("📈 Binance pronto para uso")

    # Loop principal do engine
    while True:
        print("⏳ Engine ativo — aguardando sinais...")
        time.sleep(60)


if __name__ == "__main__":
    start_engine()
