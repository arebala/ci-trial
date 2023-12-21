from breeze_connect import BreezeConnect
import time
import pandas as pd
import pickle

# Initialize SDK
breeze = BreezeConnect(api_key="33%300L2s48bz28I08#190846Qd3809e")
print("Connected")
time.sleep(1)
# Generate Session
breeze.generate_session(api_secret="7461r00e81824W51^0q17n7a8P4764#0",
                        session_token="29488172")
time.sleep(1)
# read stock symbols from Pala_Group_Companies.xlsx and store in a list
df = pd.read_excel('Pala_Group_Companies.xlsx', sheet_name='Sheet1')
stock_list = df['ICICI Stock Symbol'].tolist()
#print(stock_list)

#for each stock symbol in the stock_list, get the historical data
for stock in stock_list:
    #print(stock)
    entries = breeze.get_historical_data_v2(interval="1day",
                            from_date= "2021-01-01T07:00:00.000Z",
                            to_date= "2023-12-20T15:30:00.000Z",
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
        pickle.dump(entries, open("pickles/" + stock + ".p", "wb"))
        #print(df)
        
        # Calculate the EMA with a period of 5 days and a weighting factor of 0.2
        #df['ema'] = df['close'].ewm(span=10, adjust=False, min_periods=0).mean()

        #print(df)
        # if 'ema' in df is between close and open of the corresponding day, then print the date
        #if df['ema'].iloc[-1] > df['open'].iloc[-1] and df['ema'].iloc[-1] < df['close'].iloc[-1]:
            #print(df['datetime'].iloc[-1] + " for " + stock + " open: " + str(df['open'].iloc[-1]) + " close: " + str(df['close'].iloc[-1]) + " ema: " + str(df['ema'].iloc[-1]))
    time.sleep(1)
"""
entries = breeze.get_historical_data_v2(interval="1day",
                            from_date= "2023-10-05T07:00:00.000Z",
                            to_date= "2023-12-20T17:00:00.000Z",
                            stock_code="WIPRO",
                            exchange_code="NSE",
                            product_type="cash")
#if entries are present in  the dictionary
if 'Success' in entries:
    #print(entries['Success'])
    close_values = [entry['close'] for entry in entries['Success']]
    #print(close_values)
   
    df = pd.DataFrame(entries['Success'])

    print(df)
    # Calculate the EMA with a period of 5 days and a weighting factor of 0.2
    df['ema'] = df['close'].ewm(span=10, adjust=False, min_periods=0).mean()

    #print(df)
    # if 'ema' in df is between close and open of the corresponding day, then print the date
    if df['ema'].iloc[-1] > df['open'].iloc[-1] and df['ema'].iloc[-1] < df['close'].iloc[-1]:
        print(df['date'].iloc[-1] + " for " + df['date'].iloc[-3])

"""
"""
# Close SDK
breeze.close()
"""

"""
def waitForResourceAvailable(response, timeout, timewait):
    timer = 0
    while response.status_code == 204:
        time.sleep(timewait)
        timer += timewait
        if timer > timeout:
            break
        if response.status_code == 200:
            break
"""
#print(breeze.get_demat_holdings())
#print(breeze.get_portfolio_positions())
"""
holdings = breeze.get_portfolio_holdings(exchange_code="NSE",
                                from_date="2023-12-16T06:00:00.000Z",
                                to_date="2023-12-17T06:00:00.000Z",
                                stock_code="",
                                portfolio_type="")
print(holdings)
print(breeze.get_names(exchange_code = 'NSE',stock_code = 'TATASTEEL'))

print(breeze.get_trade_list(from_date="2023-12-01T06:00:00.000Z",
                        to_date="2023-12-17T06:00:00.000Z",
                        exchange_code="NSE",
                        product_type="",
                        action="",
                        stock_code=""))

status = breeze.place_order(stock_code = "RELIND",
    exchange_code= "NSE",
    product = "btst",
    action = "buy",
    order_type = "limit",
    quantity = "1",
    price = "2250",
    validity = "day",
    stoploss  = "",
    order_type_fresh = "",
    order_rate_fresh = "",
    validity_date = "",
    disclosed_quantity = "",
    expiry_date =  "",
    right = "",
    strike_price = "",
    user_remark = "",
    settlement_id = "2023122",
    order_segment_code = "N")

print(status)
"""
