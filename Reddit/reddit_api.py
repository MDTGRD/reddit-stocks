import requests
import os
import json
import pandas as pd

base_url = 'https://www.reddit.com/'

# Login method and credentials
data = {
    'grant_type': 'password',
    'username': os.getenv('RedditUser'),
    'password': os.getenv('RedditPW')
}

# Inputting ClientID/Personal Use Script & Token
auth = requests.auth.HTTPBasicAuth(os.getenv('RedditClientID'), os.getenv('RedditSecretToken'))

# Header info for description
headers = {'user-agent': 'analysisAPI by YoloOfDawn'}

# Requesting OAuth token
r = requests.post(base_url + 'api/v1/access_token', auth=auth, data=data, headers=headers)

# Converting response to json
d = r.json()

# Creating bearer token and adding to headers
token = 'bearer ' + d['access_token']

headers = {**headers, **{'Authorization': f"{token}"}}

res = requests.get('https://oauth.reddit.com/r/stocks/hot', headers=headers)

df = pd.DataFrame()

for post in res.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)

titles = df['title']

# Cleaning punctuation and separating into words
for char in '-.,\n':
    titles=titles.replace(char, ' ')

print(titles)

#word_list = titles.split()
#print(word_list)

# d = {}
