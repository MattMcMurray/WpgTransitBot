__author__ = 'Mathieu'

import tweepy
from bot import attempt_reply


class TwitterStreamListener (tweepy.StreamListener):

    def on_status(self, status):
        try:
            attempt_reply()

        except Exception as e:
            print 'ERROR: Fetching tweets went wrong.'
            print e.message

    def on_error(self, status_code):
        print('ERROR: Twitter returned streaming status code {0}'.format(status_code))
