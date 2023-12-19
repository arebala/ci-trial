import pandas as pd

# Create a dataset with closing prices for a stock
prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 137, 128, 111, 117, 123]
df = pd.DataFrame({'close': prices})

# Calculate the EMA with a period of 5 days and a weighting factor of 0.2
df['ema'] = df['close'].ewm(span=15, adjust=False, min_periods=0).mean()

print(df)