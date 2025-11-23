# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

async def reply_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("مرحبا")

def main():
    TOKEN = "8521693570:AAH9yg2mNj75C9QyQ0UJa3p8vAJuqblh5pg"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.ALL, reply_hello))

    print("البوت يعمل الآن... (Ctrl + C لإيقافه)")
    app.run_polling()

if __name__ == "__main__":
    main()
