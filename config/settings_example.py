# CONFIGURAÇÕES DE EXEMPLO DO ROBÔ DE TRADING

# ====== BINANCE / EXCHANGE ======
BINANCE_API_KEY = "SUA_API_KEY_AQUI"
BINANCE_API_SECRET = "SEU_API_SECRET_AQUI"
BINANCE_TESTNET = True  # vamos usar ambiente de teste, mais seguro

# ====== ATIVO PADRÃO ======
SYMBOL = "BTC/USDT"  # Par de moedas padrão
TIMEFRAME = "15m"    # Tempo do candle: 1m, 5m, 15m, 1h...

# ====== RISCO ======
RISK_MAX_LOSS_PER_DAY = 0.02  # 2% de perda máxima no dia
RISK_POSITION_SIZE = 0.01     # 1% do saldo por operação

# ====== TELEGRAM (VAMOS USAR DEPOIS) ======
TELEGRAM_BOT_TOKEN = "SEU_TOKEN_DO_BOT_AQUI"
TELEGRAM_ALLOWED_USER_ID = 123456789  # seu ID numérico do Telegram

# ====== OUTROS ======
ENGINE_LOOP_SECONDS = 60  # a cada 60 segundos o robô pensa de novo
