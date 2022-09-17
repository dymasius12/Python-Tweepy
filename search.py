from cgitb import text
import tweepy
import config
# from  write_json import load_data, save_data
# from json_csv import json_csv

FILE_NAME = 'tweets.txt'
SAVED_DATA = FILE_NAME + '.json'
JSON_FILE = SAVED_DATA
CSV_FILE = FILE_NAME + '.csv'


client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
# Query is basically the thing you are searching
# query = 'covid OR covid19 -is:retweet -has:media'
# query = 'kopi OR kopi enak OR kopi indonesia OR kopi viral OR kopi terkenal -is:retweet -has:media place_country:ID'
query = 'jual biji kopi OR jual kopi indonesia OR kopi murah OR shopee kopi OR tokopedia kopi -is:retweet -has:media'

# if you want to add specific info, goes to dev platform and search inside the fundementals.
# response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['geo.place_id', 'author_id'])
# dict with each user information
# users = {u['id']: u for u in response.includes['users']}

# this is how you get data more than 100, p.s: this is working
# with open(FILE_NAME, 'a+') as filehandler:

#     for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
#         # print(tweet.id)
#         filehandler.write('%s\n' % tweet.id)


#declare empty list
# i = 0
# all_information = load_data(SAVED_DATA)

# for tweet in response.data:
#     # i += 1

#     if places[tweet.geo['place_id']]:
#         place = places[tweet.geo['place_id']]
#         print(tweet.id)
#         print(place.full_name)
#     #making sure user has id
#     if users[tweet.author_id]:
#         user = users[tweet.author_id]
#         # Passing the value
#         userid = tweet.id
#         language = tweet.lang
#         username = user.username
#         profile_image = user.profile_image_url
#         tweet_text = tweet.text

#     # key = f'user_{i}'
#     # information = {
#     #         'ID': userid,
#     #         'language': language,
#     #         'username': username,
#     #         'profile_image': profile_image,
#     #         'tweets': tweet_text
#     # }
    
#     # all_information[key] = information
            
#     print("all_information is SAVED!")

#     print(tweet.id)
#     print(tweet.lang)
#     print(user.username)
#     print(user.profile_image_url)
#     print(tweet.text)

# save_data(SAVED_DATA, all_information)
# json_csv(JSON_FILE=JSON_FILE, CSV_FILE=CSV_FILE)