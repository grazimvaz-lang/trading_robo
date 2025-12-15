# =============================================
# CONFIGURAÇÕES DO ROBÔ DE TRADING
# =============================================

# ===== BINANCE / EXCHANGE =====
# Coloque aqui sua API REAL da Binance
BINANCE_API_KEY = "FWAy4wi5QEnBwodEU4IDiILEztyWM3TtchnIctiIIOQ7H9E1lh2StpFsOVB7g1NE"
BINANCE_API_SECRET = "IAeen9M1USK18ABWoOuWtw7RrWNLWAkrzbNvzWwWrEhhUBGwab3vuSGGyNYGaRws"

# Se False → usa conta REAL
# Se True → usa conta de TESTE (Testnet)
BINANCE_TESTNET = False


# ===== ATIVO PADRÃO =====
# Em conta REAL, nunca use "BTC/USDT"
# O formato correto é SEM BARRA: BTCUSDT, ETHUSDT...
SYMBOL = "BTCUSDT"

# Intervalo dos candles: 1m, 5m, 15m, 1h...
TIMEFRAME = "15m"


# ===== RISCO =====
# Proporção segura recomendada:
# 2% perda máxima no dia
RISK_MAX_LOSS_PER_DAY = 0.02

# 1% do saldo por operação
RISK_POSITION_SIZE = 0.01


# ===== TELEGRAM BOT =====
# Token do seu bot do BotFather
TELEGRAM_BOT_TOKEN = "8418511094:AAEwWMfNsOgeagwrZbVLMKRe_qtXQwHFvR4"

# Seu ID de usuário (Para o bot só responder seu Telegram)
TELEGRAM_ALLOWED_USER_ID = 8212732153


# ===== CONFIGURAÇÕES DO MOTOR DO ROBÔ =====
# Quantos segundos entre um ciclo e outro do robô
ENGINE_LOOP_SECONDS = 60
# Recomendo 60 a 180 para operação segura


# =============================================
# FIM DO ARQUIVO - NÃO ALTERAR ABAIXO
# =============================================
