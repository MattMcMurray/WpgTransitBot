__author__ = 'Mathieu'

import tweepy

from TwitterStreamListener import TwitterStreamListener
from Auth import API


def run():

    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=API.auth, listener=stream_listener)

    stream.filter(track=['dogs'])


run()