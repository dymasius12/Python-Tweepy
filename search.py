from cgitb import text
import tweepy
import config
from  write_json import SAVED_DATA, load_data, save_data

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
# Query is basically the thing you are searching
# query = 'covid OR covid19 -is:retweet -has:media'
# query = 'kopi OR kopi enak OR kopi indonesia OR kopi viral OR kopi terkenal -is:retweet -has:media place_country:ID'
query = 'kopi OR kopi enak OR kopi indonesia OR kopi viral OR kopi terkenal -is:retweet -has:media'

# if you want to add specific info, goes to dev platform and search inside the fundementals.
response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'])

# dict with each user information
users = {u['id']: u for u in response.includes['users']}

#declare empty list

for i, tweet in response.data:
    information = {}
    load_data(SAVED_DATA)

    if users[tweet.author_id]:
        user = users[tweet.author_id]

    userid = tweet.id
    language = tweet.lang
    username = user.username
    profile_image = user.profile_image_url
    tweet_text = tweet.text

    information = {
        f'user_{i}': [
            {
        'ID': userid,
        'language': language,
        'username': username,
        'profile_image': profile_image,
        'tweets': tweet_text
        }]
    }

    
    save_data(SAVED_DATA, information)

    print(tweet.id)
    print(tweet.lang)
    print(user.username)
    print(user.profile_image_url)
    print(tweet.text)