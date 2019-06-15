import pandas as pd

filepath = "TabSepartor_WithoutHeader.txt"

headercolumn=["sodium", "sugar", "type"]

#Load Data into variable
#Declare header as None
#Define own header
#Set index as the first Column
data = pd.read_csv(filepath, sep=" ", header=None, index_col=0, names=headercolumn)


print(data.head())