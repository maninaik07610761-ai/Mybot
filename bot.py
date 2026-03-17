import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Send Instagram / YouTube link to download")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    await update.message.reply_text("⏳ Downloading...")

    try:
        api_url = f"https://api.vevioz.com/api/button/mp4?url={url}"
        response = requests.get(api_url)

        if response.status_code == 200:
            await update.message.reply_text(f"✅ Download link:\n{api_url}")
        else:
            await update.message.reply_text("❌ Failed to fetch video")

    except Exception as e:
        await update.message.reply_text("❌ Error occurred")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))

print("Bot is running...")
app.run_polling()
