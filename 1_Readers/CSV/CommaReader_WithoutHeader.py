import pandas as pd

#Define the filepath
filepath = "CommaSeparator_WithOutHeader.csv"

#Load the file into a variable
#Declare the first column as index column
#Define the comma as separator
#Define the first row as header row
data = pd.read_csv(filepath, index_col=0, sep=",", header=0)

print(data.head())