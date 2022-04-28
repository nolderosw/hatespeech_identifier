from auth import *
from normalizer import *
from tokenizer import criar_tokens
import configparser
import pandas as pd

client = authenticate()
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

query = config['twitter']['hate_words'] + ' lang:pt -is:retweet -is:reply'
tweets = client.search_recent_tweets(query=query, max_results=100)

columns = ['Tweet Tratado', 'Tweet Original']
data = []
lista_tweets = []
lista_tweets_tratados = []

for tweet in tweets.data:
    if(tweet is not None):
        lista_tweets.append(tweet)

lista_tweets_tratados = remove_urls(lista_tweets)
lista_tweets_tratados = remove_hashtag(lista_tweets_tratados)
lista_tweets_tratados = remove_usuario(lista_tweets_tratados)
lista_tweets_tratados = criar_tokens(lista_tweets_tratados)
lista_tweets_tratados = retirar_stopwords(lista_tweets_tratados)
lista_tweets_tratados = retirar_acentos(lista_tweets_tratados)
lista_tweets_tratados = remove_unicode(lista_tweets_tratados)

for i in range(len(lista_tweets_tratados)):
    data.append([lista_tweets_tratados[i],lista_tweets[i]])


df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv', mode='a', index=False)