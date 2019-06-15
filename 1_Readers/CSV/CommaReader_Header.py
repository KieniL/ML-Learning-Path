import pandas as pd

#Define the filePath
filepath = "CommaSeparator_Header.csv"
#Import the CSV into a variable and declare the indexcolumn
#Also declare the comma as separator
data = pd.read_csv(filepath, index_col=0, sep=",")

print(data.head())
