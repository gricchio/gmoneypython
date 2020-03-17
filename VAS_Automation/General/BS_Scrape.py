'''
Created on Feb 20, 2020

@author: Gino.Ricchio
'''
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
from io import BytesIO


url = "https://eft-loot.com/"



res = requests.get(url)

soup = BeautifulSoup(res.content,'html.parser')
print(soup.prettify().encode("utf-8"))

child = list(soup.children)
print(child.encode("utf-8"))
