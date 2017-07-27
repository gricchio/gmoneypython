'''
Created on Jan 5, 2017

@author: RiccGA
'''
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas_datareader as pddr
import numpy
from pandas_datareader import data, wb
from datetime import date
from pandas import DataFrame as df
from conda._vendor.auxlib.collection import last

from scipy.stats.mstats import gmean as gm

first = datetime.datetime(2017, 5, 8)
last = datetime.datetime(2017, 5, 11)
stocks = ["AAPL",'GOOG','^GSPC']
field = 'Close'

#Functions

def date(ticker):
    histinfo = pddr.data.get_data_yahoo(ticker,start = first, end = last)
    return histinfo['Date']

def close(ticker):
    histinfo = pddr.data.get_data_yahoo(ticker,start = first, end = last)
    return histinfo[field]

def min(ticker):
    histinfo = pddr.data.get_data_yahoo(ticker,start = first, end = last)
    return histinfo[field].min()
def max(ticker):
    histinfo = pddr.data.get_data_yahoo(ticker,start = first, end = last)
    return histinfo[field].max()

def variance(ticker):
    histinfo = pddr.data.get_data_yahoo(ticker,start = first, end = last)
    close = histinfo[field]
    return numpy.var(close)

def std(ticker):
    histinfo = pddr.data.get_data_yahoo(ticker,start = first, end = last)
    close = histinfo[field]
    return numpy.std(close)

def individual(stock):
    hist = close(stock)
    histmean = sum(hist)/len(hist)
    print (stock, round(histmean,2))
    print hist

def geomean(x):
    #feed in daily changes
    base = 1
    for d in x:
        factor = 1 + float(x)
        sum = factor * base 
    return sum

# Data frame Stuff

class analysis_pack(object):
    def __init__(self, ticker, first, last):
        self.ticker = ticker
        self.first = first
        self.last = last
        self.histinfo = pddr.data.get_data_yahoo(ticker, start = self.first, end = self.last)[field].round(2)
        self.histprices = pddr.data.get_data_yahoo(ticker, start = self.first, end = self.last)[field].round(2).values.tolist()
        self.min = self.histinfo.min()
        self.max = self.histinfo.max()
        self.variance = 'pass'
        self.std = 'pass'
        self.dailychange = numpy.diff(self.histinfo).round(2)
        self.trailingday = self.histprices[0:-1]
        self.daily_prct_change = [round(float(b) / float(m),3) for b,m in zip(self.dailychange,self.trailingday)]
        #self.georeturn = geomean(self.daily_prct_change)
        
        #self.geo_rtn = gm(self.dailychange)
    
my_stock = analysis_pack('NAK', first, last)

print close('NAK')
print my_stock.trailingday
print my_stock.dailychange
print my_stock.daily_prct_change


##what function feeds in
"""
selecteddata = [variance(stocks), std(stocks)]



## Table Stuff
d1 = df(selecteddata).rename(index={0: "Variance",1: "STD"}).round(2)
print d1
"""


