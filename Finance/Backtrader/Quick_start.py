'''
Created on Dec 15, 2017

@author: RiccGA
'''
#declarations
from __future__ import (absolute_import, division, print_function, unicode_literals)
import backtrader as bt
import datetime, os.path, sys


class TestStrategy(bt.Strategy):
    
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(' %s, %s' % (dt.isoformat(), txt))
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        
        
    def next(self):
        self.log('Close, %2f' % self.dataclose[0])
        if self.order:
            return
        if not self.position:
                if self.dataclose[0] < self.dataclose[-1]:
                    if self.dataclose[-1] < self.dataclose[-2]:
                        self.log('BUY CREATE, %.2f' % self.dataclose[0])
                        self.order = self.buy()
        else:
            if len(self) >= (self.bar_executed + 5):
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.order = self.sell()
            
                   
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY Executed, %.2f, Cost: %.2f, Comm: %.2f' % 
                        (order.executed.price,
                         order.executed.value,
                         order.executed.comm
                         ))
            elif order.issell():
                self.log('SELL Executed, %.2f, Cost: %.2f, Comm: %.2f' % 
                         (order.executed.price,
                         order.executed.value,
                         order.executed.comm
                         ))
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        self.order = None
    
    
    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log('Operation Profit, Gross %.2f, Net %.2f' % (trade.pnl, trade.pnlcomm))
        
        
        
        
        
        
if __name__ == '__main__' :
    #create Cerebro entity
    cr = bt.Cerebro()
    
    # Add a strategy
    cr.addstrategy(TestStrategy)
    
    
    
        
    #locating the script
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'data/spb.csv')
    
    #create a datafeed
    
    data = bt.feeds.YahooFinanceCSVData(
        dataname = datapath,
        
        fromdate = datetime.datetime(2017,11,21),
        todate = datetime.datetime(2017,12,8),
        reverse = False)
    cr.adddata(data)
    cr.broker.setcash(100000.0)
    cr.broker.setcommission(commission=0.001)
    
    print ('Starting Portfolio Value: %.2f' % cr.broker.getvalue())
    cr.run()    
    
    
    
    
    print ('Ending Portfolio Value: %.2f' % cr.broker.getvalue())
    
