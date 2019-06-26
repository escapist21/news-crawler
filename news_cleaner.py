import pandas as pd

df = pd.read_csv('results.csv')

#df.info()


#df.name = df.name.str.rstrip('...')

#print(df.head(2))

df['time'] = df['description'].str.rstrip(' -')
print(df['time'])