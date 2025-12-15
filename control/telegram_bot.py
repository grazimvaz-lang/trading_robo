import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

print("🤖 Iniciando Bot do Telegram...")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("❌ TELEGRAM_BOT_TOKEN não definido nas variáveis de ambiente")


# ===============================
# Comandos
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Bot online!\n\n"
        "Comandos disponíveis:\n"
        "/start - iniciar bot\n"
        "/status - status do robô"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Robô ativo\n"
        "⏳ Aguardando sinais\n"
        "🚄 Rodando no Railway"
    )


# ===============================
# Inicialização
# ===============================
async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("✅ Bot do Telegram iniciado com sucesso")
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
