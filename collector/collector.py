from auth import *
from normalizer import *
from tokenizer import create_tokens
import configparser
import pandas as pd

client = authenticate()
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

query = config['twitter']['hate_words'] + ' lang:pt -is:retweet -is:reply'
tweets = client.search_recent_tweets(query=query, max_results=100)

columns = ['Tweet Tratado', 'Tweet Original']
data = []
tweets_original = []
tweets_normalized = []

for tweet in tweets.data:
    if(tweet is not None):
        tweets_original.append(tweet)

tweets_normalized = remove_urls(tweets_original)
tweets_normalized = remove_hashtag(tweets_normalized)
tweets_normalized = remove_usuario(tweets_normalized)
tweets_normalized = create_tokens(tweets_normalized)
tweets_normalized = remove_stopwords(tweets_normalized)
tweets_normalized = remove_acentos(tweets_normalized)
tweets_normalized = remove_unicode(tweets_normalized)

for i in range(len(tweets_normalized)):
    data.append([tweets_normalized[i],tweets_original[i]])


df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv', mode='a', index=False)