# WpgTransitBot
Using Winnipeg Transit's developer API and Tweepy to replicate Transit's bustxt service on Twitter

####Requirements
- You will need to have the following installed:
  - [Tweepy](https://github.com/tweepy/tweepy) (`pip install tweepy`)
  - Dateutil (`pip install python-dateutil`)
  - Pytz (for timezone adjustement) (`pip install pytz`)
  - That's it!

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
