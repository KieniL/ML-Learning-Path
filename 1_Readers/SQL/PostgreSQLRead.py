#You need the additional modul psycopg2 (Do pip install psycopg2) for postgresql
import pandas as pd
import psycopg2 as pg

#Create a connection item
engine = pg.connect("host='<IP Or Hostname>' port=<Port> dbname=<DBName> user=<User> password='<Passwd>'")

#Load QueryData into variable
data = pd.read_sql("<Query>", con=engine)

print(data.head())