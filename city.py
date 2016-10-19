# UTF-8
import requests
from bs4 import BeautifulSoup
import re
import sqlite3

r = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City', auth=('user', 'pass'))
soup = BeautifulSoup(r.text, 'html.parser')

tbl = soup.table.select("tr > td:nth-of-type(5)")

conn = sqlite3.connect('neighbors.db')
c = conn.cursor()
c.execute('CREATE TABLE nyc_table (neighbors, text)')

list = []

for entry in tbl:
	list.extend(entry.text[:].split(', '))
	
for element in list:
	c.execute("INSERT INTO nyc_table (neighbors) VALUES ('"+element+"')")

conn.commit()
conn.close()
print(list)


