from tracemalloc import start
import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# This is how to get the username and user_id of twitter account
# users = client.get_users_tweets(usernames=['getudev'])

# for user in users:
#     print(user)

# tweets = client.get_users_tweets(id=config.USER_ID, tweet_fields=['lang'])

# for tweet in tweets.data:
#     print(tweet.id)
#     print(tweet.lang)

# users = client.get_users_followers(id=config.USER_ID, user_fields=['profile_image_url'])
# for user in users.data:
#     print(user)

# users = client.get_users_following(id=config.USER_ID, user_fields=['profile_image_url'])
# for user in users.data:
#     print(user)

# get who likes a certain tweet using tweet id
# users = client.get_liking_users(id=config.TWEET_ID)
# for user in users.data:
#     print(user.username)  

# users = client.get_retweeters(id=config.TWEET_ID)
# for user in users.data:
#     print(user.id) 

# Get the tweet based on the tweet id
response = client.get_tweet(id=config.TWEET_ID, tweet_fields=['created_at'])
tweet = response.data
print(tweet.created_at)