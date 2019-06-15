#For importing Excel you need the modul xlrd (do pip install xlrd)
import pandas as pd


#Declare filepath
filepath = "WithoutHeader_WithIndex.xlsx"

headercolumn =["sodium", "sugar", "type"]
#Load Data into variable
#Declare Header=None
#Declare Header self
#Declare firstcolumn as index
data = pd.read_excel(filepath, header=None, names=headercolumn, index_column=0)

print(data.head())