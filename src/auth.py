import tweepy

# from secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from services import printlog

class Key:
    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

def getUserCreds():
    a_token = raw_input("Please enter your access token:\n")
    a_secret = raw_input("Please enter your access secret:\n")
    c_key = raw_input("Please enter your consumer key:\n")
    c_secret = raw_input("Please enter your consumer secret:\n")

    key = Key(a_token, a_secret, c_key, c_secret)

    print 'Object instatiated'
    print key.access_token
    print key.access_secret
    print key.consumer_key
    print key.consumer_secret

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

# API = authenticate()
getUserCreds()