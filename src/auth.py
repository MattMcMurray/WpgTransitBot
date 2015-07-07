import tweepy

from secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from services import printlog


def authenticate():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        #TODO fix; authentication always returns OK
        return api

    except tweepy.TweepError as e:
    	printlog("Tweepy Error while autheticating")
        printlog(e.message)
        return False

API = authenticate()