import requests
import os

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

res.json(())

for post in res.json()['data']['children']:
    print(post['data']['title'])