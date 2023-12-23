from breeze_connect import BreezeConnect
import time
import pandas as pd
import pickle
import datetime as dt

# Initialize SDK
breeze = BreezeConnect(api_key="33%300L2s48bz28I08#190846Qd3809e")
print("Connected")
time.sleep(1)
# Generate Session
breeze.generate_session(api_secret="7461r00e81824W51^0q17n7a8P4764#0",
                        session_token="29770677")
time.sleep(1)
# read stock symbols from Pala_Group_Companies.xlsx and store in a list
df = pd.read_excel('Pala_Group_Companies.xlsx', sheet_name='Sheet1')
stock_list = df['ICICI Stock Symbol'].tolist()

# Get the current date
current_date = dt.datetime.now().date()

# Format the date as a string
formatted_date = current_date.strftime('%Y-%m-%d')


# Construct the file name
file_name = f'profit/profit_{formatted_date}.csv'
print(file_name)

total_profit = 0
total_invested_amount = 0
for stock in stock_list:
    #print(stock)
    entries = breeze.get_historical_data_v2(interval="1day",
                            from_date= "2023-12-11T07:00:00.000Z",
                            to_date= "2023-12-21T15:30:00.000Z",
                            stock_code=stock,
                            exchange_code="NSE",
                            product_type="cash")
    #print(entries)
    #if entries are present in  the dictionary
    if 'Success' in entries:
        close_values = [entry['close'] for entry in entries['Success']]
        
        df = pd.DataFrame(entries['Success'])

        # if the dataframe is empty, then skip the stock
        if df.empty:
            print("Empty dataframe for " + stock)
            continue
        #pickle the entries dictionary for each stock symbol in the stock_list to a file in pickles directory
        #pickle.dump(entries, open("pickles/" + stock + ".p", "wb"))
        #print(df)
        
        # Calculate the EMA with a period of 5 days and a weighting factor of 0.2
        df['ema'] = df['close'].ewm(span=10, adjust=False, min_periods=0).mean()

        #print(df)
        # if 'ema' in df is between close and open of the corresponding day, then print the date
        print(stock)
        if df['ema'].iloc[-1] > df['open'].iloc[-1] and df['ema'].iloc[-1] < df['close'].iloc[-1]:
            #print(df['datetime'].iloc[-1] + " for " + stock + " open: " + str(df['open'].iloc[-1]) + " close: " + str(df['close'].iloc[-1]) + " ema: " + str(df['ema'].iloc[-1]))
            today_entry = breeze.get_quotes(stock_code=stock,
                    exchange_code="NSE",
                    expiry_date="2023-12-22T16:00:00.000Z",
                    product_type="cash",
                    right="others",
                    strike_price="0")
            #today_ltp = int(today_entry['Success'][0]['ltp'])
            #print(today_ltp)
            profit = int(today_entry['Success'][0]['ltp']) - int(df['close'].iloc[-1])
            profit_percent = (profit / int(df['close'].iloc[-1])) * 100
            #round the profit to 2 decimal places
            profit_percent = round(profit_percent, 2)
            total_profit = total_profit + profit
            total_invested_amount = total_invested_amount + int(df['close'].iloc[-1])
            print(stock + " profit: " + str(profit) + " total_profit: " + str(total_profit))
            # create a csv for recodring profit and total profit along with stock code for the day. Create csv file with date from 'datetime' column. Append the profit and total profit to the csv file, if the file exists
            #file_name = "profit/" + df['datetime'].iloc[-1].split(' ')[0] + ".csv"
            #file_name = "profit/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".csv"
            open = df['close'].iloc[-1]
            close = today_entry['Success'][0]['ltp']
            # Construct the file name
            #file_name = f'profit_{formatted_date}.csv'
            print(file_name)

            try:
                df1 = pd.read_csv(file_name)
            except FileNotFoundError:
                df1 = pd.DataFrame(columns=['Stock', 'Open', 'Close', 'Profit', 'Profit Percent'])

                df1.to_csv(file_name, index=False, header=True, mode='w')
            df1 = pd.DataFrame([[stock, open, close, profit, profit_percent]], columns=['Stock', 'Open', 'Close', 'Profit', 'Profit Percent'])
            df1.to_csv(file_name, index=False, header=False, mode='a')
    time.sleep(1)
# add last row to the csv file with total profit and total invested amount
    # file name with today's date
#file_name = "profit/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".csv"
#file_name = "profit/" + df['datetime'].iloc[-1].split(' ')[0] + ".csv"
df1 = pd.DataFrame([[total_profit, total_invested_amount]], columns=['Total Profit', 'Total Invested Amount'])
df1.to_csv(file_name, index=False, header=True, mode='a')

#print(entry)