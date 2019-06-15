#For importing Excel you need the modul xlrd (do pip install xlrd)
import pandas as pd

#Declare the filepath
filepath = "WithoutHeader_WithoutIndex.xlsx"


headercolumn= ["sodium", "sugar", "type"]

#Load Data into variable
#Declare NullHeader
#Declare headerColumns
data = pd.read_excel(filepath, header=None, names=headercolumn)

print(data.head())