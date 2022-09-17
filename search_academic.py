from tracemalloc import start
import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = 'covid -is:retweet'

start_time = '2020-01-01T00:00:00Z'

end_time = '2020-05-01T00:00:00Z'

# Basically this is how to implement time search
response = client.search_all_tweets(query=query, max_result=100, start_time=start_time, end_time=end_time)

for tweet in response.data:
    print(tweet.id)

