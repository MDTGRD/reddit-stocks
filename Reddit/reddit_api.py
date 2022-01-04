import requests
import os
import json
import pandas as pd

pd.set_option('display.max_rows', None)

def authentication():

    '''
    Creating token authentication for Reddit API.

    Args: 
        arg_1 (str): 

    Returns: 
        str: Return the authentication token as a string

    Raises: 
    '''

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

    return headers

def api_to_df():

    '''
    Utilized the authorization to generate data through API call

    Args: 
        arg_1 (str): 

    Returns: 
        str: Return requested data through a Pandas dataframe

    Raises: 
    '''

    # Requesting data from the API
    res = requests.get('https://oauth.reddit.com/r/stocks/top/?t=year', headers=headers)

    # Creating dataframe object
    df = pd.DataFrame()

    # Appending data to dataframe
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

    return df

def stock_regex():

    '''
    Manipulating the result of the dataframe using regex

    Args: 
        arg_1 (str): 

    Returns: 
        str: Filtered list & counts of words that match regex

    Raises: 
    '''

    # Replacing punctuations
    df["df_new"] = df['title'].str.replace('[^\w\s]','')

    # Splitting column into separate words and counting them
    new_df = df.df_new.str.split(expand=True).stack().value_counts().reset_index()

    # Creating and applying regex to filter capitalized 4-letter words
    regex = "[A-Z]{4}"

    new_df = new_df[new_df['index'].str.match(regex)]

    return new_df

def main(): 
    headers = authentication()
    df = api_to_df()
    new_df = stock_regex()

if __name__ == '__main__':
    main()