import pandas as pd
import sqlite3

conn = sqlite3.connect('api_yamdb.db')
c = conn.cursor()
users = pd.read_csv('titles.csv')
users.to_sql('titles', conn, if_exists='append', index=False)
