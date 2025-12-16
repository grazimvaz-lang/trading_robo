from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
import os
import asyncio
import logging

# ===============================
# CONFIGURAÇÃO DE LOG
# ===============================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# ===============================
# TOKEN DO TELEGRAM
# ===============================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN não encontrado nas variáveis de ambiente")

# ===============================
# COMANDOS DO BOT
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Robô de negociação ONLINE!\n\n"
        "Estou rodando 24h no Railway.\n"
        "Aguardando
