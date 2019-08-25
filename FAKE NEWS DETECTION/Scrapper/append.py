import pandas as pd

a = pd.read_csv("bbc_news.csv")
b = pd.read_csv("IndiaTimes.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='fake')
merged.to_csv("output.csv", index=False)