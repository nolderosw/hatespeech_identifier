import re
import nltk
import string
import unicodedata

def retirar_stopwords(lista_tweets):
    stopwords = nltk.corpus.stopwords.words("portuguese")

    regex = re.compile('[%s]' % re.escape(string.punctuation))
    nova_lista = []

    for index in range(len(lista_tweets)):
        nova_lista.append([])
        for palavra in lista_tweets[index]:
            nova_palavra = regex.sub(u'', palavra)
            if not nova_palavra == u'' and nova_palavra not in stopwords and not bool(re.search(r'\d', palavra)) and palavra != "RT":
                nova_lista[index].append(nova_palavra)

    return nova_lista


def retirar_acentos(lista_tweets):
    texto_limpo = []
    for indice in range(len(lista_tweets)):
        texto_limpo.append([])
        for palavra in lista_tweets[indice]:
            nfkd = unicodedata.normalize('NFKD', palavra)
            palavra_sem_acento = u''.join([c for c in nfkd if not unicodedata.combining(c)])
            q = re.sub('[^a-zA-Z0-9 \\\]', ' ', palavra_sem_acento)

            texto_limpo[indice].append(q.lower().strip())

    return texto_limpo


def remove_hashtag(lista_tweets):
    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"#\S+", "", tweet)
        novos_tweets.append(texto)

    return novos_tweets


def remove_usuario(lista_tweets):
    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"@\S+", "", tweet)
        novos_tweets.append(texto)

    return novos_tweets


def remove_urls(lista_tweets):
    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"http\S+", "", tweet["text"])
        novos_tweets.append(texto)

    return novos_tweets


def remove_unicode(lista_tweets):
    nova_lista = []
    for indice, palavras in enumerate(lista_tweets):
        nova_lista.append([])
        for palavra in palavras:
            if palavra != '':
                nova_lista[indice].append(str(palavra))
    return nova_lista