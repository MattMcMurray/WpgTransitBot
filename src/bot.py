import tweepy
import logging

from services import printlog, getlogdir, clearlogs
from auth import API
from transit_api import get_next_arrival


class TwitterStreamListener (tweepy.StreamListener):

    def on_status(self, status):
        try:
            printlog("Received new tweet: ")
            printlog(status.text)
            parse_input(status)

        except Exception as e:
            printlog('ERROR: Fetching tweets went wrong.')
            printlog(e.message)

    def on_error(self, status_code):
        printlog('ERROR: Twitter returned streaming status code {0}'.format(status_code))


def run():
    startupmsg = "Find a bug? Want to request a feature? -> github.com/MattMcMurray/WpgTransitBot/issues"

    printlog('Starting...')
    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=API.auth, listener=stream_listener)

    try:
        API.update_status(status=startupmsg)
    except Exception as e:
        printlog("Could not send startupmsg:")
        printlog(e.message)

    while True:

        try:
            printlog('Tracking tweets...')

            stream.filter(track=['@WpgTransitBot'])

        except AttributeError as e:
            printlog("Attribute error; this seems to be a bug with StreamListener:")
            printlog(e.message)
            continue

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
        printlog("Error while processing user's input:")
        printlog(e.message)

    send_reply(tweet, msg)

def send_reply(reply_to_tweet, msg_body):
    username = reply_to_tweet.user.screen_name
    tweet_id = reply_to_tweet.id
    #
    # msg = "Your tweet was received"
    #
    # API.update_status(status=msg, in_reply_to_status_id=)

    message = "@{0} {1}".format(username, msg_body)

    printlog(message)
    API.update_status(status=message, in_reply_to_status_id=tweet_id)
    printlog('Message sent!')


if __name__ == '__main__':
    clearlogs()
    errorfile = getlogdir()
    errorfile += 'error.log'
    logging.basicConfig(level=logging.DEBUG, filename=errorfile)

    try:
        run()
    except Exception as e:
        printlog('UNHANDLED EXCEPTION:')
        printlog(e.message)
        logging.exception(e)

