# auto_run.py
import time
from core.engine import TradingEngine
from config import settings


def main():
    """
    Loop automático do robô.
    Executa um ciclo, espera alguns segundos e repete para sempre.
    """
    engine = TradingEngine()

    print("🤖 Iniciando loop automático do robô...")
    print(f"Par: {settings.SYMBOL} | Timeframe: {settings.TIMEFRAME}")
    print(f"Intervalo entre ciclos: {settings.ENGINE_LOOP_SECONDS} segundos\n")

    try:
        while True:
            print("\n--- Novo ciclo automático ---")
            signal = engine.run_once()   # sua estratégia roda aqui

            print(f"SINAL: {signal}")
            print(
                f"Aguardando {settings.ENGINE_LOOP_SECONDS} segundos "
                "para o próximo candle..."
            )

            time.sleep(settings.ENGINE_LOOP_SECONDS)

    except KeyboardInterrupt:
        # Quando você apertar CTRL + C, ele sai com elegância
        print("\n⛔ Loop interrompido manualmente. Encerrando robô...")


if __name__ == "__main__":
    main()
