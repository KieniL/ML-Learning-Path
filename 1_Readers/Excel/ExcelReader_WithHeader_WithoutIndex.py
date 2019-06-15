#For importing Excel you need the modul xlrd (do pip install xlrd)
import pandas as pd

#Declare the filepath
filepath = "WithHeader_WithoutIndex.xlsx"


#Load file into variable
data = pd.read_excel(filepath)

print(data.head())