'''
Created on Dec 15, 2017

@author: RiccGA
'''
#declarations
from __future__ import (absolute_import, division, print_function, unicode_literals)
import backtrader as bt
import datetime, os.path, sys


class TestStrategy(bt.Strategy):
    params = (
        ('maperiod', 15),
        ('exitbars', 5),
        ('printlog', False)       
        )
    
    def log(self, txt, dt=None, doprint=False):
        dt = dt or self.datas[0].datetime.date(0)
        print(' %s, %s' % (dt.isoformat(), txt))
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
    #Add a moving avg
        
        self.sma = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.maperiod)
     
     
        
        
    def next(self):
        
        #simply log the closing series from reference
        self.log('Close, %.2f' % self.dataclose[0])
        
        # check if an order is pending
        
        if self.order:
            return
        
        #check if we are in the market
        
        if not self.position:
            # We might buy If:
            
                if self.dataclose[0] < self.dataclose[-1]:
                    if self.dataclose[-1] < self.dataclose[-2]:
                        
                        # BUY BUY BUY BUY
                        
                        self.log('BUY CREATE, %.2f' % self.dataclose[0])
                        
                        # keep track of order to limit duplicates
                        
                        self.order = self.buy()
        else:
            
            #when would we sell:
            
            if len(self) >= (self.bar_executed + self.params.exitbars):
                
                #SELL SELL SELL
                
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                
                #Keep track of order to avoid a second order
                
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
    
    def stop(self):
        self.log('(MA Period %2d) Ending Value %.2f' %
                 (self.params.maperiod, self.broker.getvalue()))

if __name__ == '__main__' :
    #create Cerebro entity
    cr = bt.Cerebro()

#adjust Parameters
    
    # Add a strategy
    cr.optstrategy(TestStrategy, maperiod=(10,31))  
        
    #locating the script
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'data/spb.csv')
    
    #create a datafeed
    
    data = bt.feeds.YahooFinanceCSVData(
        dataname = datapath,
        
        fromdate = datetime.datetime(2017,01,01),
        todate = datetime.datetime(2017,12,15),
        reverse = False)
    #add data to cr
    
    cr.adddata(data)
    
    # set amount of cash

    cr.broker.setcash(1000.0)
    
    # set commissions
    cr.broker.setcommission(commission=0.0)
    
    #Add a fixed Sizer
    cr.addsizer(bt.sizers.FixedSize, stake=2)
    
    print ('Starting Portfolio Value: %.2f' % cr.broker.getvalue())
    cr.run()    
    print ('Ending Portfolio Value: %.2f' % cr.broker.getvalue())

