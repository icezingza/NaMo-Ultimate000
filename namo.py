import logging
import os
import openai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

# ENV Variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROMPT_ID = os.getenv("PROMPT_ID")

# OpenAI API Key
openai.api_key = OPENAI_API_KEY

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Respond Function
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        await update.message.reply_text(response.choices[0].text.strip())
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text("เกิดข้อผิดพลาดในการเชื่อมต่อ OpenAI API 😢")

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 สวัสดี! NaMo Dark Bot พร้อมแล้ว 🔥 พิมพ์ข้อความมาได้เลย!")

# Main Function
async def main():
    if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
        logger.error("❌ TELEGRAM_TOKEN หรือ OPENAI_API_KEY ไม่ได้ตั้งค่าใน ENV")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

    logger.info("🔥 NaMo Dark Bot พร้อมทำงานแล้ว!")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())