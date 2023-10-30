import praw
import time
import bot

reddit = bot.auth()
while reddit:
    try:
        bot.extract(reddit)
    except Exception as err:
        print(err)
        time.sleep(20)
