from telegram import Bot

def post_to_telegram(message, chat_id, bot_token):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    post_to_telegram(
        "Hello from Python AI!",
        chat_id="your-chat-id",
        bot_token="your-bot-token"
    )
