from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the actual token from BotFather
TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your Telegram bot.')

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
