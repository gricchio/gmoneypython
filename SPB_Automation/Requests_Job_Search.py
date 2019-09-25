'''
Created on Aug 13, 2019

@author: 200460
'''

import requests
import requests.auth
import pprint
import json

reddit_app_id = 'googledrive - Python Test Materials'
reddit_secret = 'googledrive - Python Test Materials'
reddit_id = 'googledrive - Python Test Materials'
reddit_pass = 'googledrive - Python Test Materials'
headers = {"User-Agent" : "Gmoney Reddit Bot by Gmoney"}
reddit_access_token_url = "https://www.reddit.com/api/v1/access_token"
limit = 4



client_auth = requests.auth.HTTPBasicAuth(reddit_app_id, reddit_secret)
post_data = {"grant_type" : "password", "username" : reddit_id, "password": reddit_pass}

response = requests.post(reddit_access_token_url, auth=client_auth, data=post_data, headers = headers)
r = response.json()


headers = {"Authorization" : "bearer " + r['access_token'], "User-Agent" : "Gmoney Reddit Bot by Gmoney"}
parameters = {'limit' : limit}


response = requests.get("https://oauth.reddit.com/r/funny/hot", headers=headers, params = parameters)

python_obj = json.loads(response.content)
#print python_obj
#print python_obj[u'data'][u'children']

file_links = []
"""
for post in python_obj:
    file_links.append(post)

    
print file_links
"""
pprint.pprint(response.json())


