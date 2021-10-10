from bs4 import BeautifulSoup as bs
import requests
from requests_html import HTMLSession
import sqlite3
import pandas as pd
import datetime

connection = sqlite3.connect('laptop.db')
c = connection.cursor()

c.execute('''CREATE TABLE Tracker(Date DATE, Name TEXT, price REAL, Savings REAL)''')

urls = ["https://www.amazon.in/gp/product/B091HGK1B6/ref=ox_sc_act_title_1?smid=A372Y0DOIAPTGJ&psc=1"]

for url in urls:   

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }

    session = HTMLSession()
    r = session.get(url, headers = header)
    r.html.render(sleep = 1,timeout=10)

    current_date = datetime.datetime.now()
    title = r.html.find('#productTitle', first=True).text.strip()[:25]
    Cost = r.html.find('#priceblock_ourprice', first=True).text.strip()[1:]
    Savings = r.html.find('.priceBlockSavingsString', first=True).text.strip()[1:]
    c.execute('''INSERT INTO Tracker VALUES(?,?,?,?)''', (current_date, title, Cost, Savings))

connection.commit()

db = pd.read_sql_query("SELECT * FROM Tracker", connection)
print(db)
connection.close()


