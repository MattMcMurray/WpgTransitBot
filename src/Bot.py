__author__ = 'Mathieu'

import tweepy

from TwitterStreamListener import TwitterStreamListener
from Auth import API
from Database import connect, close
from datetime import datetime


def run():

    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=API.auth, listener=stream_listener)

    stream.filter(track=['@WpgTransitBot'])

    return


def reply(tweet):

    if validate_user(tweet.user):
        # send_reply(user.id)
        print

    return


def validate_user(user):

    cursor, connection = connect()

    # Check if the user has been banned for abusing the service
    query = "SELECT * FROM users WHERE uID = {0}".format(user)
    data = cursor.execute(query)
    data = cursor.fetchone()
    last_reply_time = data[1]
    user_banned = data[2]
    user_warned = data[3]

    if user_banned != 1:

        diff = datetime.now() - last_reply_time

        if diff.total_seconds() <= 60:
            if user_warned == 1:
                # send the warning
                print 'WARNING'

        else:
            print 'neat'

    return


if __name__ == '__main__':
    run()