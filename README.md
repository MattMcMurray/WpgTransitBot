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
The bot now asks for your API keys!

Everytime the bot runs, it will ask if you'd like to load previously stored credentials. If it is your first time running the bot, you'll have to input your keys. If you've already run the bot and saved your creds, they'll be stored for future use and you can load those on each run. 

<i>(This is a temporary solution, eventually I plan on creating a way to input these on the first run or use a .config file)</i>

#### Future Features
- Abuse checking: Make sure users aren't spamming the bot
- Extended modes: Search for nearby stops, get more than 1 result back, etc
- Automatic Reminders: Ask the bot to remind you 15, 30, 45mins before a bus is scheduled to arrive
