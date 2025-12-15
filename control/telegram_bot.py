import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from config import settings
from core.engine import TradingEngine

engine = TradingEngine()

async def start(update, context):
    await update.message.reply_text("🤖 Bot ativo!")

async def status(update, context):
    await update.message.reply_text(f"SINAL ATUAL: {engine.last_signal}")

async def main():
    print("🤖 Iniciando Bot do Telegram...")

    app = (
        ApplicationBuilder()
        .token(settings.TELEGRAM_BOT_TOKEN)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    # ⛔ NÃO FECHA LOOP – evita erro "event loop already running"
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    # Mantém bot vivo sem fechar event loop
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
