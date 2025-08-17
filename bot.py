import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext

# Bot Token aur Owner ID ko Environment Variables se load karein
# Isse aapka token code mein hardcode nahi hoga aur secure rahega
BOT_TOKEN = os.environ.get("8403449640:AAHQ610N3BuEAFwghpd7x9PleclCpnb7i3Q")

# Owner's Telegram User ID. Apni ID yahan daalein ya environment variable se lein
OWNER_ID = int(os.environ.get("2031314339")

# Reaction emojis
REACTIONS = ['👍', '❤️', '🔥', '😂', '🤯']

def start(update: Update, context: CallbackContext) -> None:
    # Check if the user is the owner
    if update.message.from_user.id == OWNER_ID:
        keyboard = [
            [
                InlineKeyboardButton("Support Channel", url="https://t.me/Yaaron_Ki_Baatein"),
                InlineKeyboardButton("Support Group", url="https://t.me/Yaaron_Ki_Baatein")
            ],
            [
                InlineKeyboardButton("Broadcast", callback_data="broadcast")
            ]
        ]
    else:
        keyboard = [
            [
                InlineKeyboardButton("My Other Bots", url="https://t.me/divyansh_botz"),
                InlineKeyboardButton("Support Group", url="https://t.me/divyansh_support")
            ]
        ]
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "👋 Hello! I am an auto-reaction bot.",
        reply_markup=reply_markup
    )

def handle_message(update: Update, context: CallbackContext) -> None:
    try:
        # Get the message object, whether it's a regular message or a channel post
        message = update.channel_post or update.message
        if message:
            chat_id = message.chat_id
            message_id = message.message_id
            
            # React to the message with a thumbs up
            context.bot.set_message_reaction(
                chat_id=chat_id,
                message_id=message_id,
                reaction=REACTIONS[0]
            )
            
    except Exception as e:
        print(f"Error while reacting: {e}")
        
def broadcast(update: Update, context: CallbackContext) -> None:
    # This command is for the owner only
    if update.message.from_user.id != OWNER_ID:
        update.message.reply_text("You are not authorized to use this command.")
        return

    # To implement a full broadcast feature, you'll need a database to store user IDs.
    # For now, this is a placeholder.
    update.message.reply_text("Broadcast feature needs a database setup. Please add one to your code.")


def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN:
        print("BOT_TOKEN environment variable not set. Please set it.")
        return

    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("broadcast", broadcast))
    dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
