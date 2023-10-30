from decouple import config
import praw
import time
import requests
import random

def auth():
    reddit = praw.Reddit(
     client_id=config("client_id"),
     client_secret=config("client_secret"),
     password=config("password"),
     username=config("username"),
     user_agent=config("user_agent")
    )
    print("logged into reddit successfully")
    return reddit



def extract(reddit):
    with open('subreddits.txt', 'r+') as subs:
        f = subs.read()
    try:
        subreddit = reddit.subreddit(f)
        for submission in subreddit.hot(limit=25):
             x = submission.url
             r = requests.get(x, allow_redirects=True)
             for i in range(0,1):
                open(f'./img/{random.random()}.jpg', 'wb').write(r.content)
        print("<----done---->")
        print("downloaded")
        print("<----sugoi---->")
        exit(0)
    except Exception as err:
        print(err)
        time.sleep(20)


