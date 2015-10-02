import os
import tweepy
import pickle

from services import printlog
import keyWrapper


def getUserCreds():
    print '*********************'
    print '*** Twitter OAuth ***'
    print '*********************'
    a_token = raw_input("Please enter your access token:\n")
    a_secret = raw_input("Please enter your access secret:\n")
    c_key = raw_input("Please enter your consumer key:\n")
    c_secret = raw_input("Please enter your consumer secret:\n")

    print '*********************'
    print '***  Wpg Transit  ***'
    print '*********************'
    wpg_transit_key = raw_input("Please enter you wpg transit API key:\n")

    key = keyWrapper.Key(a_token, a_secret, c_key, c_secret, wpg_transit_key)
    printlog("Instatiated key object")

    return key

def authenticate():
    # get the absolute path of this file to avoid relative path weirdness
    here = os.path.dirname(os.path.abspath(__file__))
    resource_dir = '{0}/../res/'.format(here)
    key_filename = 'key.pkl'

    try:
        key = keyWrapper.getKeyObj()

    except IOError as ioe:
        print "Something went wrong during file I/O"
        print "Exiting..."
        exit()

    else:
        printlog("Keys successfully loaded")

        if key is not None:

            try:
                auth = tweepy.OAuthHandler(
                    key.consumer_key, 
                    key.consumer_secret
                    )
                auth.set_access_token(
                    key.access_token, 
                    key.access_secret)

                api = tweepy.API(auth)

                #TODO fix; authentication always returns OK
                return api

            except tweepy.TweepError as e:
            	printlog("Tweepy Error while autheticating")
                printlog(e.message)
                return False

        else:
            printlog("There was some sort of error loading the API keys")


if __name__ == "__main__":

    response = raw_input("Would you like to load previously used API keys? [y/n]")

    if (response == 'y' or response == 'yes'):

        if keyWrapper.doesKeyExist():
            authenticate()
        else:
            key = getUserCreds()
            keyWrapper.saveKeyObj(key)

    else:
        key = getUserCreds()
        keyWrapper.saveKeyObj(key)
        authenticate()

