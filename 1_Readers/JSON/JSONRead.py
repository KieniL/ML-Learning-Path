import pandas as pd

filepath = "winemag-data-130k-v2.json"

#load data into variable
#read json converts object into rows
data = pd.read_json(filepath)

print(data.head())