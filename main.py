import pandas

url = "http://www.smgov.net/inspections.csv"

print("Downloading data...")

df = pandas.read_csv(url)

print(df.info())

print(df.head(5))
