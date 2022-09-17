import tweepy
import config

# this is example of creating a tweet and liking a tweet or etc.
client = tweepy.Client(consumer_key=config.API_KEY, consumer_secret=config.API_SECRET,access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)

response = client.create_tweet(text='Hello World!')

print(response)