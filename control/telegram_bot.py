import os
import time

try:
    from telegram import Update
    from telegram.ext import (
        ApplicationBuilder,
        CommandHandler,
        ContextTypes
    )
except Exception as e:
    print("⚠️ Telegram desativado:", e)
    ApplicationBuilder = None

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Robô online com sucesso!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Status: robô ativo e aguardando sinais.")

def main():
    if not ApplicationBuilder:
        print("⚠️ Biblioteca do Telegram não disponível.")
        return

    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN não definido.")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("✅ Bot do Telegram iniciado")
    app.run_polling()

if __name__ == "__main__":
    main()
