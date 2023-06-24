#multiple pages scraping!
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url = "https://www.flipkart.com/q/best-laptops-under-rs-50000"

page = requests.get(url)

soup = bs(page.text, 'lxml')

df = pd.DataFrame({'name':[],'price':[],'rating':[],'rating_count':[]})

counter = 0

while counter<=10:
    postings = soup.find_all('div',class_='_3pLy-c row')
    for i in postings:
        try:
            name = i.find('div',class_='_4rR01T').text
            price = i.find('div',class_='_30jeq3 _1_WHN1').text
            rating = i.find('div',class_='_3LWZlK').text
            rating_count = i.find('span',class_='_2_R_DZ').text
            df = df.append({'name':name,'price':price,'rating':rating,'rating_count':rating_count}, ignore_index=True)
        except:
            pass
        
    next_page = soup.find('a', class_='_1LKTO3').get('href')
    next_page_full = "https://www.flipkart.com"+next_page
    url = next_page_full
    page = requests.get(url)
    soup = bs(page.text, 'lxml')
    counter+=1
    
file = df.to_csv(r"C:\Users\navv\Desktop\pagination.csv")