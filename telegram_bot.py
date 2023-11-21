from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from faker import Faker

# Replace 'YOUR_BOT_TOKEN' with the actual token from BotFather
TOKEN = '6413717643:AAEwBBXr1b9VAP7O5x-ghzFd4N95B38MUGE'

fake = Faker()

# Dictionary to store user accounts
user_accounts = {}

class User:
    def __init__(self, user_id, name, email, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_accounts:
        update.message.reply_text("Please create an account first using the /createaccount command.")
    else:
        user = user_accounts[user_id]
        update.message.reply_text(f'Hello, {user.name}! I am your Telegram bot.')

def create_account(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_accounts:
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()

        user_accounts[user_id] = User(user_id, name, email, phone)

        user_info = f"Name: {name}\nEmail: {email}\nPhone: {phone}"
        update.message.reply_text(f"Your Dummy Account Information:\n{user_info}")
    else:
        update.message.reply_text("You already have an account. Use /start to interact with the bot.")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("createaccount", create_account))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
