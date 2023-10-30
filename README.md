## Reddit bot

reddit bot which **downloads** "hot" posts of the given subreddits.

### Dependencies

```
pip install -r requirements.txt

```
### Installation

1) Sign in with your reddit account
2) Go [here](https://www.reddit.com/prefs/apps/) and create an app
3) Generate a new OAuth token and add the tokens in the .env file

Create a .env file 
```
  client_id="your_client_id"
  client_secret="your_client_secret"
  password="your_password"
  user_agent="your_user_agent"
  username="your_username"

```

In between those quotes, you have to add your tokens which you generated previously.

### Usage
Once you are done with adding the creds, you can execute the bot
```
python main.py
```
Hopefully at this point, you might see "logged into reddit successfully" message being displayed.
The images will be downloaded in the img folder.
### Additionals

1) You can add your favourite subreddits in the subreddits.txt.
2) You can alter the limit size for the posts


