'''
Created on Apr 20, 2020

@author: Gino.Ricchio
'''
import requests
import json
from pprint import pprint


#import username and password
auth_file = r'C:\Users\gino.ricchio\Desktop\Python Projects\Turnips\docs.txt'
docs = open(auth_file,'r').read().split('\n')
username = docs[0]
print(username)
password = docs[1]
print(password)
user_pass_dict = {
    'user': username,
    'passwd': password,
    'api_type': 'json'}
headers = {'user-agent': 'Gmoneys API test',}

#access reddit's API
print(user_pass_dict['passwd'])
client = requests.session()
client.headers = headers
r = client.post(r'https://ssl.reddit.com/api/login', data=user_pass_dict)
pprint(r.content)
j = json.loads(r.content)

