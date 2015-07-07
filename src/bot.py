__author__ = 'Mathieu'

import tweepy

from auth import API
from transit_api import get_next_arrival


class TwitterStreamListener (tweepy.StreamListener):

    def on_status(self, status):
        try:
            print "Received tweet: ", status.text
            parse_input(status)

        except Exception as e:
            print 'ERROR: Fetching tweets went wrong.'
            print e.message

    def on_error(self, status_code):
        print('ERROR: Twitter returned streaming status code {0}'.format(status_code))


def run():

    print 'Starting...'
    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=API.auth, listener=stream_listener)

    stream.filter(track=['@WpgTransitBot'])

    print 'Tracking tweets...'

    return


def parse_input(tweet):
    msg = "I'm sorry, I didn't understand that. Tweets must be in this format: " \
          "<stop #> <route #> (or that bus/stop combo doesn't exist)"

    tweet_text = tweet.text

    try:
        user, stopnum, routenum = tweet_text.split()
        arrival = get_next_arrival(int(stopnum), int(routenum))
        msg = "The next {0} arrives at stop number {1} at {2}".format(routenum, stopnum, arrival.time())

    except Exception as e:
        print "Error while processing user's input"
        print e.message

    send_reply(tweet, msg)

# for the future:
# def validate_user(user_id):
#
#     cursor, connection = connect()
#
#     valid_user = False
#
#     # Check if the user has been banned for abusing the service
#     query = "SELECT * FROM users WHERE uID = {0}".format(user_id)
#     data = cursor.execute(query)
#     data = cursor.fetchone()
#     last_reply_time = data[1]
#     user_banned = data[2]
#     user_warned = data[3]
#
#     if user_banned != 1:
#         valid_user = True
#
#         diff = datetime.now() - last_reply_time
#
#         if diff.total_seconds() <= 60:
#             if user_warned == 1:
#                 # send the warning
#                 print 'WARNING'
#
#         else:
#             print 'neat'
#
#     cursor.close()
#     connection.close()
#
#     return valid_user


def send_reply(reply_to_tweet, msg_body):
    username = reply_to_tweet.user.screen_name
    tweet_id = reply_to_tweet.id
    #
    # msg = "Your tweet was received"
    #
    # API.update_status(status=msg, in_reply_to_status_id=)

    message = "@{0} {1}".format(username, msg_body)

    print message
    API.update_status(status=message, in_reply_to_status_id=tweet_id)
    print 'Message sent!'


if __name__ == '__main__':
    run()

