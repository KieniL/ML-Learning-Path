import pandas as pd

filepath = "TabSeparator_Header.txt"

#Load Data into variable
#Define Space as separator (also for Tab)
#Set Index to None
data = pd.read_csv(filepath, sep=" ", index_col=None)


print(data.head())