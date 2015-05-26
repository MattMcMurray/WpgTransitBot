__author__ = 'Mathieu'

import tweepy

from TwitterStreamListener import TwitterStreamListener
import Auth

def run():

    api = Auth.authenticate()

    myStreamListener = TwitterStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    myStream.filter(track = ['dogs'])

run()