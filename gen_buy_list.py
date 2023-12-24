"""
read stock entries from pickles directory one file at a time and 
calculate the EMA on rolling basis for the previous 5 days and 
compare it with the close value of the current day check if the 
EMA is between the open and close values of the current day. If 
EMA falls between the open and close values of the current day, 
where the open value is less than the close value, then add the
stock symbol to the buy list.
Buy list must contain the stock symbol, the date on which the
EMA was between the open and close values of the current day
and the open and close values of the current day.
Create a pickle file for the buy list on per date basis.
"""

#import first_connect
import pandas as pd
import pickle
import time
import datetime
import os.path

# read stock symbols from Pala_Group_Companies.xlsx and store in a list
df = pd.read_excel('Pala_Group_Companies.xlsx', sheet_name='Sheet1')
stock_list = df['ICICI Stock Symbol'].tolist()

# read the stock symbols from the stock_list file
# stock_list = open("stock_list", "r").read().splitlines()
# print(stock_list)
# print(len(stock_list))

# create a list for the buy list
buy_list = []
# create a dictionary for the stock entries
entries = []

# read stock entries from pickles directory one file at a time
for stock in stock_list:
    # check if the file exists
    if not os.path.isfile("pickles/stock_prices/" + stock + ".p"):
        continue
    
    entries = pickle.load(open("pickles/stock_prices/" + stock + ".p", "rb"))
    #print(entries)
    # if entries are present in  the dictionary
    if 'Success' in entries:
        df = pd.DataFrame(entries['Success'])
        # print(df)
        # Calculate the EMA with a period of 5 days and a weighting factor of 0.2
        df['ema'] = df['close'].ewm(span=10, adjust=False, min_periods=0).mean()
        #print(df)
        # walk through the dataframe and check if the EMA is between the open and close values for each day in the dataframe
        for index, row in df.iterrows():
            # if 'ema' in df is between close and open of the corresponding day, then print the date
            if row['ema'] > row['open'] and row['ema'] < row['close']:
                """
                # print(df['date'].iloc[-1] + " for " + df['date'].iloc[-3])
                # add the stock symbol to the buy list
                buy_list.append(stock)
                # add the stock symbol, the date on which the EMA was between the open and close values of the current day
                # and the open and close values of the current day to the buy list
                buy_list.append(row['datetime'])
                buy_list.append(row['open'])
                buy_list.append(row['close'])
                # create a pickle file for the buy list on per date basis
                pickle.dump(buy_list, open("pickles/buy_list/" + row['datetime'] + ".p", "wb"))
                # print(buy_list)
                """
                #print(stock + "," + row['datetime'].split(' ')[0] + "," + str(row['open']) + "," + str(row['close']))
                
                #write stock, datetime, open, close to a csv file. remove time from datetime
                with open("buy_list.csv", "a") as f:
                    f.write(stock + "," + row['datetime'].split(' ')[0] + "," + str(row['open']) + "," + str(row['close']) + "\n")
                # clear the buy list
                #buy_list = []
        """
        # if 'ema' in df is between close and open of the corresponding day, then print the date
        if df['ema'].iloc[-1] > df['open'].iloc[-1] and df['ema'].iloc[-1] < df['close'].iloc[-1]:
            # print(df['date'].iloc[-1] + " for " + df['date'].iloc[-3])
            # add the stock symbol to the buy list
            buy_list.append(stock)
            # add the stock symbol, the date on which the EMA was between the open and close values of the current day
            # and the open and close values of the current day to the buy list
            buy_list.append(df['date'].iloc[-1])
            buy_list.append(df['open'].iloc[-1])
            buy_list.append(df['close'].iloc[-1])
            # create a pickle file for the buy list on per date basis
            pickle.dump(buy_list, open("buy_list/" + df['date'].iloc[-1] + ".p", "wb"))
            # print(buy_list)
            # clear the buy list
            buy_list = []
        """
    else:
        print("No entries for " + stock)
    time.sleep(1)


    
    