import pandas as pd
#For Mysql you need the MySQLdb (do pip install MySQLdb)
import MySQLdb

#Define a MySQLConnection
mysql_cn = MySQLdb.connect(host="<ip or Host>", port=3307,
                           user="<user>", passwd="<pwd",
                           db="<db>")


#Declare the Query and the MySQL Connector
#Declare the Indexcolumn based on the index column from the query
data = pd.read_sql( "<query>", con=mysql_cn, index_col="id")

print(data.head())