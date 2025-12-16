from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_TOKEN
from state import ligar, desligar, status

def start(update, context):
    update.message.reply_text(
        "🤖 Robô online.\n\n"
        "Comandos disponíveis:\n"
        "/on  → ligar robô\n"
        "/off → desligar robô\n"
        "/status → ver status"
    )

def on(update, context):
    ligar()
    update.message.reply_text("✅ Robô LIGADO (24h).")

def off(update, context):
    desligar()
    update.message.reply_text("⛔ Robô DESLIGADO.")

def stat(update, context):
    s = "LIGADO ✅" if status() else "DESLIGADO ⛔"
    update.message.reply_text(f"📊 Status atual: {s}")

def iniciar_bot():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("on", on))
    dp.add_handler(CommandHandler("off", off))
    dp.add_handler(CommandHandler("status", stat))

    updater.start_polling()
