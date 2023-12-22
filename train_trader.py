"""
a portfolio of stocks where stocks are purchased from buy_list 
and sold after a certain period of time when the price is higher 
than the purchase price by 10% or more or sold when the price is
down by 5% or more.
Stock code, purchase price, purchase date, number of stocks, sell 
price, sell date, profit/loss need to be stored in a pickle file
"""
import os
import pickle
import pandas as pd
import time
import datetime
import breeze_client
import breeze_client.api
import breeze_client.model
from breeze_client.api import DefaultApi
from pprint import pprint
from datetime import datetime
from stock_class import Stock

# open the pickle files from the buy_list directory and walk the buylist directory 
# and buy stocks and store in Stock from class
def create_buy_list():
    buy_list = []
    for root, dirs, files in os.walk("buy_list"):
        for file in files:
            if file.endswith(".p"):
                with open(os.path.join(root, file), "rb") as f:
                    buy_list.append(pickle.load(f))
    return buy_list

# walk the buy list and buy 3 quantities of each stock and store the stock in a list 
# using Stock class object for recording stock code, quantity, purchase date
def buy_stocks(buy_list):
    stock_list = []
    for stock in buy_list:
        stock_code = stock[0]
        stock_price = stock[1]
        stock_date = stock[2]
        stock_quantity = 3
        stock_list.append(Stock(stock_code, stock_price, stock_date, stock_quantity))
    return stock_list

def main():
    # create the buy list
    buy_list = create_buy_list()
    # buy stocks from the buy list
    stock_list = buy_stocks(buy_list)
    # print the stock list
    total_invested_amount = 0
    for stock in stock_list:
        total_invested_amount = total_invested_amount + stock.calculate_average_buy_price()
    print(total_invested_amount)
    
    """
    # walk the stock list and sell stocks when the price is higher than the purchase price by 10% or more
    for stock in stock_list:
        stock.calculate_profit_loss(10)

        
    # sell stocks from the stock list
    for stock in stock_list:
        stock.sell_stock()
    """
if __name__ == "__main__":  
    main()