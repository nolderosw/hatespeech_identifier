from csv import writer
from csv import reader
from normalizer import *
from tokenizer import create_tokens
import pandas as pd

with open('treinamento.csv', 'r') as read_obj, \
        open('treinamento_1.csv', 'w', newline='') as write_obj:
    csv_reader = reader(read_obj)
    csv_writer = writer(write_obj)
    lista_tweets = []
    classification = []
    data = []
    columns = ['Classificacao','Tweet Tratado', 'Tweet Original']
    for row in csv_reader:
        lista_tweets.append(row[0].split(';')[2])
        classification.append(row[0].split(';')[1])
    
    tweets_normalized = remove_hashtag(lista_tweets)
    tweets_normalized = remove_usuario(tweets_normalized)
    tweets_normalized = create_tokens(tweets_normalized)
    tweets_normalized = remove_stopwords(tweets_normalized)
    tweets_normalized = remove_acentos(tweets_normalized)
    tweets_normalized = remove_unicode(tweets_normalized)


    for i in range(len(tweets_normalized)):
        data.append([classification[i],tweets_normalized[i],lista_tweets[i]])


    df = pd.DataFrame(data, columns=columns)
    df.to_csv('treinamento_1.csv', mode='a', index=False)