'''
Created on Mar 2, 2020

@author: Gino.Ricchio
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

url = 'https://eft-loot.com/'

res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')

comments = soup.find_all(string=lambda text: isinstance(text, Comment))

tables = []
for each in comments:
    if 'table' in each:
        try:
            tables.append(pd.read_html(each)[0])
        except:
            continue

"""
table = soup.find_all('table')
df = pd.read_html(str(table))

print(df[0].to_json(orient='records'))
"""

print(tables)