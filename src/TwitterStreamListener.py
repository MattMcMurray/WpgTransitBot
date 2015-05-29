__author__ = 'Mathieu'

import tweepy
from Bot import reply


class TwitterStreamListener (tweepy.StreamListener):

    def on_status(self, status):
        try:
            reply()

        except Exception as e:
            print 'ERROR: Fetching tweets went wrong.'
            print e.message

    def on_error(self, status_code):
        print('ERROR: Twitter returned streaming status code {0}'.format(status_code))
