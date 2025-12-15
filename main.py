import subprocess
import time

print("🤖 Iniciando Engine + Telegram Bot...")

# Caminho do Python correto (venv)
PYTHON = r"./venv/Scripts/python.exe"

# Inicia o engine em um processo separado
subprocess.Popen([PYTHON, "-m", "core.engine"])

# Espera 2 segundos antes de iniciar o bot
time.sleep(2)

# Inicia o bot do Telegram
subprocess.Popen([PYTHON, "-m", "control.telegram_bot"])
