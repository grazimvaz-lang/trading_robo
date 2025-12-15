import subprocess
import time
import sys

print("🤖 Iniciando Engine + Telegram Bot...")

PYTHON = sys.executable  # pega o python correto do ambiente

# Inicia o engine
print("🔌 Iniciando Engine...")
subprocess.Popen([PYTHON, "-m", "core.engine"])

time.sleep(2)

# Inicia o bot do Telegram
print("🤖 Iniciando Bot do Telegram...")
subprocess.Popen([PYTHON, "-m", "control.telegram_bot"])
