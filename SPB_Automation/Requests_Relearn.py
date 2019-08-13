'''
Created on Aug 12, 2019

@author: 200460
'''

import requests

#http://httpbin.org/#/Auth/get_basic_auth__user___passwd_ << good resource for testing
#need to set a timeout as request will wait forever for a response


"""

r = requests.get('https://httpbin.org/basic-auth/Gino/testing', auth=('Gino','testing'), timeout= 3)

print r.status_code
print r.text

"""

r = requests.get('https://httpbin.org/delay/6', timeout= 7)

print r.status_code










"""

<<Get requests with a payload and pulling back
payload = {
    'page' : 2,
    'count' : 25,    
    }

r = requests.get('https://httpbin.org/get', params=payload)

#print r.text
print r.url
"""

"""
<<<Posting Data and dissecting it
payload = {
    'username' : 'Gino',
    'password' : 'testing',    
    }

r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()

print r_dict['form']
#print r.url


"""




#print(help(r))
#print(dir(r))
#print(r.status_code)
"""
Need to check if you are checking a website, not sure if the request was a success
Http Status codes
200 - Success Code
300 - Redirect
400 - Client Error
500 - Server Error
"""

#print r.headers

#print (r.ok)
#True if you get less than 400 (successful)

"""

Pulls down an image and saves it
with open('comic.png', 'wb') as f:
        f.write(r.content)
        #'wb' Means write bytes, input of r.content is in bites
"""