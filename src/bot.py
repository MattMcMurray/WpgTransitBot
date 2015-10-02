import tweepy
import logging
import thread

from services import printlog, getlogdir, clearlogs

import auth
import transit_api

DUPLICATE_MSG_ERR = 187


class TwitterStreamListener (tweepy.StreamListener):

    def on_status(self, status):
        try:
            handle_msg(status)
        except Exception as e:
            printlog('ERROR: Fetching tweets went wrong.')
            printlog(e.message)

    def on_error(self, status_code):
        printlog('ERROR: Twitter returned streaming status code {0}'.format(status_code))


def run():
    startupmsg = "Find a bug? Want to request a feature? -> github.com/MattMcMurray/WpgTransitBot/issues"

    printlog('Starting...')
    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=TWITTER_API.auth, listener=stream_listener)

    try:
        TWITTER_API.update_status(status=startupmsg)
    except Exception as e:
        printlog("Could not send startupmsg:\n\tcode {0} -- {1}".format(e.message[0]['code'], e.message[0]['message']))

        # If the error is not a 'duplicate status' error, exit
        if (e.message[0]['code'] != DUPLICATE_MSG_ERR):
            exit()

    while True:

        try:
            printlog('Tracking tweets...')
            stream.filter(track=['@WpgTransitBot'])

        except AttributeError as e:
            printlog("Attribute error; this seems to be a bug with StreamListener:")
            printlog(e.message)
            continue

    return


def handle_msg(status):
    printlog("Received new tweet: ")
    printlog(status.text)
    reply_msg = build_reply(status)
    send_reply(status, reply_msg)


def build_reply(tweet):
    msg = "I'm sorry, I didn't understand that. Tweets must be in this format: " \
          "<stop #> <route #> (or that bus/stop combo doesn't exist)"

    tweet_text = tweet.text

    try:
        user, stopnum, routenum = tweet_text.split()
        arrival = transit_api.get_next_arrival(int(stopnum), int(routenum))
        msg = "The next {0} arrives at stop number {1} at {2}".format(routenum, stopnum, arrival.time())

    except Exception as e:
        printlog("Error while processing user's input:")
        printlog(e.message)

    return msg


def send_reply(reply_to_tweet, msg_body):
    username = reply_to_tweet.user.screen_name
    tweet_id = reply_to_tweet.id

    message = "@{0} {1}".format(username, msg_body)

    printlog(message)
    TWITTER_API.update_status(status=message, in_reply_to_status_id=tweet_id)
    printlog('Message sent!')


if __name__ == '__main__':
    clearlogs()
    errorfile = getlogdir()
    errorfile += 'error.log'
    logging.basicConfig(level=logging.DEBUG, filename=errorfile)

    try:
        TWITTER_API = auth.authenticate()
        run()
    except Exception as e:
        printlog('UNHANDLED EXCEPTION:')
        printlog(e.message)
        logging.exception(e)
