#table scraping!
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://www.worldometers.info/world-population/india-population/"

page = requests.get(url)

soup = bs(page.text, 'lxml')

table = soup.find('table',class_='table table-striped table-bordered table-hover table-condensed table-list')

headers = []

for i in table.find_all('th'):
    title = i.text
    headers.append(title)
    
df = pd.DataFrame(columns=headers)
    
for j in table.find_all('tr')[1:]:
    rows = j.find_all('td')
    data = [tr.text for tr in rows]
    
    length = len(df)
    df.loc[length] = data
    
df.to_csv(r"C:\Users\navaneethangn\Desktop\table.csv")