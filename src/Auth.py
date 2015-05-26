__author__ = 'Mathieu'

import tweepy

from Secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def authenticate():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        return api

    except tweepy.TweepError as e:
        print e.message
        return False

API = authenticate()
