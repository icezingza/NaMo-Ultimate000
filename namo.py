import logging
import os
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# ENV Variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROMPT_ID = os.getenv("PROMPT_ID")

# OpenAI API Key
openai.api_key = OPENAI_API_KEY

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Respond Function
def respond(update: Update, context: CallbackContext):
    user_input = update.message.text
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Prompt ID {PROMPT_ID}: {user_input}",
            max_tokens=500,
            temperature=0.9,
        )
        reply_text = response.choices[0].text.strip()
        update.message.reply_text(reply_text)
    except Exception as e:
        logger.error(f"Error: {e}")
        update.message.reply_text("❌ Error: ไม่สามารถตอบได้ในตอนนี้ ลองใหม่อีกครั้งนะครับ.")

# Start Function
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 ยินดีต้อนรับสู่ NaMo Dark Bot 🔥 พร้อมรับทุกข้อความแล้ว!")

# Main
def main():
    if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
        logger.error("❌ TELEGRAM_TOKEN หรือ OPENAI_API_KEY ไม่ได้ตั้งค่าใน ENV")
        return
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
