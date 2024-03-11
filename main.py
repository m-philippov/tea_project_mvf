import backtrader as bt

import backtrader.feeds as btfeeds
import pandas as pd
import yfinance as yf
import datetime

class tetSTG(bt.Strategy):
    def __init__(self):
        pass
    def next(self):
        pass

class testClose(bt.Strategy):
    def __init__(self):
        pass
    def next(self):
        dataclose = self.datas[0].close[0]
        print(dataclose)
class testClosei(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close
    def next(self):
        print(self.dataclose[0])
class testLog(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close
    def log(self,txt):
        dt = self.datas[0].datatime.datatime()
        print(f'{dt} | {txt}')
    def next(self):
        x = self.dataclose[0]
        self.log(txt=x)

class Momentum(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close
    def next(self):
        if self.dataclose[-2] > self.dataclose[-1]:
            self.order = self.buy()
            print(f'buy executed @ {self.dataclose[0]}')
        if self.dataclose[-2] < self.dataclose[-1]:
            self.order = self.sell()
            print(f'sell executed @ {self.dataclose[0]}')
        else:
            self.order = self.close()
            print(f'closing @ {self.dataclose[0]}')

if __name__ == '__main__':
    ticker_df = yf.download(tickers='TSLA')
    ticker_df_parsed = btfeeds.PandasData(
        dataname= ticker_df, 
        datetime=None,
        open=0,
        high=1,
        low=2,
        close=4,
        volume=5,
        openinterest=-1
        )
    ticker_df.to_csv('tsla.csv')
    
    #cerebro = bt.Cerebro() #init BackTrader
    ticker_csv_parsed = btfeeds.GenericCSVData(
        dataname= 'tsla.csv', 
        dtformat= '%Y-%m-%d',
        fromdate=datetime.datetime(2023, 1, 1),
        todate=datetime.datetime(2024, 1, 1),
        datetime=0,
        open=1,
        high=2,
        low=3,
        close=5,
        volume=6,
        openinterest=-1,

        
        separator = ','
        )
    cerebro = bt.Cerebro()
    cerebro.adddata(ticker_csv_parsed)
    cerebro.addstrategy(Momentum)
    cerebro.run()
    cerebro.plot()
