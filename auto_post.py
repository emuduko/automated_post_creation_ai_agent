from generate_post import generate_post
from post_to_telegram import post_to_telegram
from post_to_x import post_to_x
import schedule
import time

def run_all():
    topic = "Tips for working from home"
    post = generate_post(topic)
    print("Generated Post:", post)

    post_to_telegram(post, chat_id="your-chat-id", bot_token="your-bot-token")

    post_to_x(
        post,
        api_key="your_api_key",
        api_secret="your_api_secret",
        access_token="your_access_token",
        access_token_secret="your_access_secret"
    )

# To test once
# run_all()

# To schedule daily at 10:00 AM
schedule.every().day.at("10:00").do(run_all)

while True:
    schedule.run_pending()
    time.sleep(60)
