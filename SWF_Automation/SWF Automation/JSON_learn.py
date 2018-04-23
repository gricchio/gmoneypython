'''
Created on Apr 19, 2018

@author: RiccGA
'''
import json, requests

url = 'https://en.wikipedia.org/w/api.php '


parameters = dict(
   titles = 'Scream',
    format=json
    )

resp = requests.get(url=url, params=parameters)
data = json.loads(resp.text)

print data