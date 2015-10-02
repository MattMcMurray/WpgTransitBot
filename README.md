# WpgTransitBot
Using Winnipeg Transit's developer API and Tweepy to replicate Transit's bustxt service on Twitter

####Requirements
- It's a good idea to install these dependencies inside a `virtualenv`
- You will need to have the following installed:
  - [Tweepy](https://github.com/tweepy/tweepy)
  - Dateutil
  - Pytz
- I've included two scripts to make life easier:
  - First, run `setup.sh` to prepare the environment and install dependencies
  - Next, run `startbot.sh` to set your API keys and run the bot
  - That's it!

####Authentication
The bot now asks for your API keys!

Everytime the bot runs, it will ask if you'd like to load previously stored credentials. If it is your first time running the bot, you'll have to input your keys. If you've already run the bot and saved your creds, they'll be stored for future use and you can load those on each run. 


#### Future Features
- Abuse checking: Make sure users aren't spamming the bot
- Extended modes: Search for nearby stops, get more than 1 result back, etc
- Automatic Reminders: Ask the bot to remind you 15, 30, 45mins before a bus is scheduled to arrive
