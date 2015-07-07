# WpgTransitBot
Using Winnipeg Transit's developer API and Tweepy to replicate Transit's bustxt service on Twitter

####Requirements
- It's a good idea to install these dependencies inside a virtualenv (`pip install virtualenv`)
- You will need to have the following installed:
  - [Tweepy](https://github.com/tweepy/tweepy) (`pip install tweepy==3.2.0`)
    - due to a known issue in the newest version of Tweepy, make sure to use V3.2.0
  - Dateutil (`pip install python-dateutil`)
  - Pytz (for timezone adjustement) (`pip install pytz`)
- I've included a `requirements.txt` file to make life easier
  - `cd` into WpgTransitBot dir and run `pip install -U -r requirements.txt`

####Authentication
To set up Twitter's/Tweepy's authentication, create a Python file (Secrets.py) in the source directory with the following:

```python
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'

TRANSIT_API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
```

<i>(This is a temporary solution, eventually I plan on creating a way to input these on the first run or use a .config file)</i>

#### Future Features
- Abuse checking: Make sure users aren't spamming the bot
- Extended modes: Search for nearby stops, get more than 1 result back, etc
- Automatic Reminders: Ask the bot to remind you 15, 30, 45mins before a bus is scheduled to arrive
