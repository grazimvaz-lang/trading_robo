from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_LIGADO = False
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Robô online.\n\n"
        "Comandos disponíveis:\n"
        "/on  - ligar robô\n"
        "/off - desligar robô\n"
        "/status - ver status"
    )


async def on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_LIGADO
    BOT_LIGADO = True
    await update.message.reply_text("✅ Robô LIGADO (24h).")


async def off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_LIGADO
    BOT_LIGADO = False
    await update.message.reply_text("⏸️ Robô DESLIGADO.")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = "🟢 Robô LIGADO" if BOT_LIGADO else "🔴 Robô DESLIGADO"
    await update.message.reply_text(texto)


def iniciar_bot():
    if not TOKEN:
        print("❌ TELEGRAM_TOKEN não configurado")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("on", on))
    app.add_handler(CommandHandler("off", off))
    app.add_handler(CommandHandler("status", status))

    print("🤖 Bot do Telegram iniciado")
    app.run_polling()


def robo_ligado():
    return BOT_LIGADO
