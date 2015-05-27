__author__ = 'Mathieu'

import tweepy


class TwitterStreamListener (tweepy.StreamListener):

    def on_status(self, status):
        try:
            print(status.text)

        except Exception as e:
            print 'Something went wrong'
            print e.message


    def on_error(self, status_code):
        print('ERROR: Twitter returned streaming status code {0}'.format(status_code))
