import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())


# Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace = True)

