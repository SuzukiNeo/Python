import requests
import json
import sys
import yfinance as yf

# Over View
# arg1: Code
# arg2/arg3: Fromdate/ToDate

# get param
Symbol = sys.argv[1]

def main():
    ticker_info = yf.Ticker(Symbol)
    # print stock info
    # print(ticker_info.info)

    # print stock price
    # print(ticker_info.history(period="max"))

    # print stock dividend
    # print(ticker_info.dividends)

    # print stock split
    # print(ticker_info.splits)

    # print annualy financials
    # print(ticker_info.financials)

    # print quarterly financials
    # print(ticker_info.quarterly_financials)

    # print major holders
    # print(ticker_info.major_holders)

    # print annualy B/S
    # print(ticker_info.balance_sheet)

    # print quarterly B/S
    # print(ticker_info.quarterly_balance_sheet)

    # print annualy CF
    # print(ticker_info.cashflow)

    # print quarterly CF
    # print(ticker_info.quarterly_cashflow)

    # print annualy earnings
    # print(ticker_info.earnings)
    
    # print quarterly earnings
    # print(ticker_info.quarterly_earnings)

if __name__ == "__main__":
    main()