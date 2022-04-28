import nltk 

def criar_tokens(lista_tweets):
    tokens = [nltk.word_tokenize(tweet) for tweet in lista_tweets]

    return tokens