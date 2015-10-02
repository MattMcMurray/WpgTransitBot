import os
import tweepy
import pickle
import pprint

from services import printlog

class Key:
    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

def getUserCreds():
    print '*********************'
    print '*** Twitter OAuth ***'
    print '*********************'
    a_token = raw_input("Please enter your access token:\n")
    a_secret = raw_input("Please enter your access secret:\n")
    c_key = raw_input("Please enter your consumer key:\n")
    c_secret = raw_input("Please enter your consumer secret:\n")

    key = Key(a_token, a_secret, c_key, c_secret)
    printlog("Instatiated key object")

    return key

def authenticate():
    print 'authenticating'
    # get the absolute path of this file to avoid relative path weirdness
    here = os.path.dirname(os.path.abspath(__file__))
    resource_dir = '{0}/../res/'.format(here)
    key_filename = 'key.pkl'

    if not os.path.exists(resource_dir):
        os.makedirs(resource_dir)

    if os.path.isfile(resource_dir + key_filename):
        key_file = open(resource_dir+key_filename, 'r')
        key = pickle.load(key_file)

    else:
        key = getUserCreds()
        key_file = open(resource_dir+key_filename, 'wb')
        pickle.dump(key, key_file)


        # try:
        #     auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
        #     auth.set_access_token(key.access_token, key.access_secret)
        #     api = tweepy.API(auth)

        #     #TODO fix; authentication always returns OK
        #     return api

        # except tweepy.TweepError as e:
        # 	printlog("Tweepy Error while autheticating")
        #     printlog(e.message)
        #     return False

# API = authenticate()
authenticate()