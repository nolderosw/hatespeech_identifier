from auth import *
import configparser
import tweepy
import pandas as pd

client = authenticate()
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

query = config['twitter']['hate_words'] + ' lang:pt -is:retweet -is:reply'
tweets = client.search_recent_tweets(query=query, max_results=10)

columns = ['Tweet']
data = []

for tweet in tweets.data:
    if(tweet is not None):
        data.append([tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv', mode='a', index=False)