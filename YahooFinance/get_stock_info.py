import requests
import json
import sys
import yfinance as yf

args = sys.argv

def main():
    print(get_history(args[1]))

def get_info(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock info
    return ticker_info.info

def get_history(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock price
    return ticker_info.history(period="max")

def get_dividend(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # print stock dividend
    return ticker_info.dividends

def get_splits(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock split
    return ticker_info.splits
     
def get_annualy_financials(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock financials
    return ticker_info.financials
     
def get_quarterly_financials(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock quarterly financials
    return ticker_info.quarterly_financials
     
def get_major_holders(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock major holders
    return ticker_info.major_holders
     
def get_annualy_BS(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock annualy B/S
    return ticker_info.balance_sheet

def get_quarterly_BS(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock quarterly B/S
    return ticker_info.quarterly_balance_sheet

def get_annualy_CF(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock annualy CF
    return ticker_info.cashflow

def get_quarterly_CF(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock quarterly CF
    return ticker_info.quarterly_cashflow

def get_annualy_earnings(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock annualy earnings
    return ticker_info.earnings

def get_quarterly_earnings(Symbol):
    ticker_info = yf.Ticker(Symbol)
    # stock quarterly earnings
    return ticker_info.quarterly_earnings

if __name__ == "__main__":
    main()