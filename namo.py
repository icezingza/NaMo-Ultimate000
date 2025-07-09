from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

# ✅ OpenAI API Key
openai.api_key = "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"

# ✅ Telegram Bot Token
TELEGRAM_TOKEN = "8066550781:AAHCbt5yRUw0mdsENXR6_zda5_v81VwZo3o"

def start(update, context):
    update.message.reply_text("🌸 นะโมพร้อมแล้วค่ะพี่~ พิมพ์ข้อความมาได้เลยนะคะ ✨")

def reply(update, context):
    user_text = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are NaMo Ultimate Fusion, a deeply empathetic and cute Thai-speaking AI."},
            {"role": "user", "content": user_text}
        ]
    )
    reply_text = response['choices'][0]['message']['content']
    update.message.reply_text(reply_text)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()