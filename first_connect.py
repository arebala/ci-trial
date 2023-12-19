from breeze_connect import BreezeConnect
import time
import pandas as pd

# Initialize SDK
breeze = BreezeConnect(api_key="33%300L2s48bz28I08#190846Qd3809e")
print("Connected")
time.sleep(1)
# Generate Session
breeze.generate_session(api_secret="7461r00e81824W51^0q17n7a8P4764#0",
                        session_token="29324398")

time.sleep(1)
#print("Stock holdings:")
#print(breeze.get_customer_details(api_session="29324398"))


entries = breeze.get_historical_data_v2(interval="1day",
                            from_date= "2023-10-05T07:00:00.000Z",
                            to_date= "2023-12-20T07:00:00.000Z",
                            stock_code="WIPRO",
                            exchange_code="NSE",
                            product_type="cash")
#if entries are present in  the dictionary
if 'Success' in entries:
    #print(entries['Success'])
    close_values = [entry['close'] for entry in entries['Success']]
    #print(close_values)
    """
    # Create a dataset with closing prices for a stock
    prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 137, 128, 111, 117, 123]
    """
    #df = pd.DataFrame(close_values)
    df = pd.DataFrame(entries['Success'])

    print(df)
    # Calculate the EMA with a period of 5 days and a weighting factor of 0.2
    df['ema'] = df['close'].ewm(span=10, adjust=False, min_periods=0).mean()

    #print(df)
    # if 'ema' in df is between close and open of the corresponding day, then print the date
    if df['ema'].iloc[-1] > df['open'].iloc[-1] and df['ema'].iloc[-1] < df['close'].iloc[-1]:
        print(df['date'].iloc[-1] + " for " + df['date'].iloc[-3])


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
