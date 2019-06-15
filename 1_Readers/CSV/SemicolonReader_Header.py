import pandas as pd

#Define the filepath
filepath = "SemicolonSeparator_Header.csv"

#Load the file into a variable
#Declare the first column as index column
#Declare the separator as semicolon
data = pd.read_csv(filepath, index_col=0, sep=";")

print(data.head())