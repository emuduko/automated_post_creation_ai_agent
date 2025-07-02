import tweepy

def post_to_x(content, api_key, api_secret, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(status=content)

if __name__ == "__main__":
    post_to_x(
        "Hello world from AI and Python!",
        api_key="your_api_key",
        api_secret="your_api_secret",
        access_token="your_access_token",
        access_token_secret="your_access_secret"
    )
