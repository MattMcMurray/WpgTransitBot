__author__ = 'Mathieu'

import tweepy


class TwitterStreamListener (tweepy.StreamListener):

    def on_status(self, status):
        # user_input = status.text
        # # process(user_input) TODO
        # print user_input
        try:
            print(status.text)
        except Exception as e:
            print 'Something went wrong'
            print e.message

