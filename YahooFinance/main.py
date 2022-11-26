import requests
import json
import sys
import yfinance as yf
import get_stock_info
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
args = sys.argv

def main():
    data = ((shiftday(args[1],0) - shiftday(args[1],args[2])) / shiftday(args[1],args[2])).reset_index()
    x=data['Date']
    y=data['Open']
    showchart(x,y,args[1])

def showchart(x,y,title):
    plt.plot(x,y,label=title)
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def shiftday(Ticker,days):
    ticker=DataFrame(get_stock_info.get_history(Ticker))
    return ticker.shift(int(days))

if __name__ == "__main__":
    main()