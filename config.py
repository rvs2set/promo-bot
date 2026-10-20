import os
from dotenv import load_dotenv
# переменные из файла .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_URL = "sqlite+aiosqlite:///bot.db"
