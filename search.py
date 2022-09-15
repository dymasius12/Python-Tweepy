import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
# Query is basically the thing you are searching
# query = 'covid OR covid19 -is:retweet -has:media'
query = 'covid OR covid19 -is:retweet -has:media'

response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], expansions=['author_id'])

for tweet in response.data:
    print(tweet.id)
    print(tweet.lang)