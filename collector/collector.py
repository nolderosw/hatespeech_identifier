from auth import *
import tweepy

client = authenticate()

query = 'odio -is:retweet -is:reply'
tweets = client.search_recent_tweets(query=query, max_results=10)
for tweet in tweets.data:
    print(tweet.text, '\n')