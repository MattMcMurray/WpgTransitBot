__author__ = 'Mathieu'

import tweepy

from twitter_stream_listener import TwitterStreamListener
from auth import API
from database import connect, close
from datetime import datetime


def run():

    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=API.auth, listener=stream_listener)

    stream.filter(track=['@WpgTransitBot'])

    return


def attempt_reply(tweet):

    if validate_user(tweet.user):
        # send_reply(user.id)
        print

    return


def validate_user(user_id):

    cursor, connection = connect()

    valid_user = False

    # Check if the user has been banned for abusing the service
    query = "SELECT * FROM users WHERE uID = {0}".format(user_id)
    data = cursor.execute(query)
    data = cursor.fetchone()
    last_reply_time = data[1]
    user_banned = data[2]
    user_warned = data[3]

    if user_banned != 1:
        valid_user = True

        diff = datetime.now() - last_reply_time

        if diff.total_seconds() <= 60:
            if user_warned == 1:
                # send the warning
                print 'WARNING'

        else:
            print 'neat'

    cursor.close()
    connection.close()

    return valid_user


def send_reply(reply_to_tweet):
    username = reply_to_tweet.screen_name
    tweet_id = reply_to_tweet.id

    msg = "Your tweet was received"

    API.update_status(status=msg, in_reply_to_status_id=)


if __name__ == '__main__':
    run()