import tweepy
import logging
from config_bot import create_api
from firehose import save_tweet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class ColombiaStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        save_tweet(tweet)

    def on_error(self, status):
        print("Error detected")


def main():
    api = create_api()
    tweets_listener = ColombiaStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(locations=[-76, 0.5, -70, 12])

if __name__ == "__main__":
    main()
