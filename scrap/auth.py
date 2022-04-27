import configparser
import tweepy

def authenticate():

    # read config
    config = configparser.ConfigParser(interpolation=None)
    config.read('config.ini')

    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']
    bearer_token = config['twitter']['bearer_token']

    # authenticate
    client = tweepy.Client(bearer_token=bearer_token, access_token=access_token, access_token_secret=access_token_secret)

    return client