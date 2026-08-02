
import os

print("🚀 Crypto AI Bot запущен!")

token = os.getenv("TELEGRAM_BOT_TOKEN")
api_key = os.getenv("BYBIT_API_KEY")
api_secret = os.getenv("BYBIT_API_SECRET")

if token:
    print("✅ Telegram Token найден")
else:
    print("❌ Telegram Token не найден")

if api_key:
    print("✅ Bybit API Key найден")
else:
    print("❌ Bybit API Key не найден")

if api_secret:
    print("✅ Bybit Secret Key найден")
else:
    print("❌ Bybit Secret Key не найден")
