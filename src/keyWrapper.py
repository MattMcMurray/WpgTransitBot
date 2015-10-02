import os
import pickle

here = os.path.dirname(os.path.abspath(__file__))
resource_dir = '{0}/../res/'.format(here)
key_filename = 'key.pkl'

class Key:
    def __init__(self, access_token, access_secret, consumer_key, consumer_secret, wpg_transit_key):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.wpg_transit_key = wpg_transit_key

def getKeyObj():
	key = None

	if doesKeyExist():
		key_file = open(resource_dir + key_filename, 'r')
		key = pickle.load(key_file)

	return key

def saveKeyObj(key):
	if not os.path.exists(resource_dir):
		os.makedirs(resource_dir)

	key_file = open(resource_dir + key_filename, 'wb')
	pickle.dump(key, key_file, pickle.HIGHEST_PROTOCOL)

def doesKeyExist():
	return os.path.isfile(resource_dir + key_filename)

