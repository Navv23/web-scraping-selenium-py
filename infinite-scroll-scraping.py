#scraping ininite scrolling!
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from selenium.webdriver.common.by import By

options = Options()
options.binary_location =r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path= r"D:\SELENIUM-TUTORIAL\chromedriver.exe")

driver.get("https://www.nike.com/in/w/mens-shoes-nik1zy7ok")

driver.maximize_window()

time.sleep(2)

soup = bs(driver.page_source, 'lxml')

postings = soup.find_all('div',class_='''product-card__info disable-animations for--product''')

while True:
    driver.execute_script('window.scrollBy(0, 5000)')
    time.sleep(2)
    soup = bs(driver.page_source, 'lxml')
    postings = soup.find_all('div',class_='''product-card__info disable-animations for--product''')
    
    df = pd.DataFrame({'name':[],'category':[],'color':[]})

    for i in postings:
        try:
            name = i.find('div',class_='product-card__title').text
            category = i.find('div', class_='product-card__subtitle').text
            color = i.find('div', class_='product-card__product-count font-override__body1').text
            mrp = i.find('div', class_='product-price in__styling is--current-price css-11s12ax')
            df = df.append({'name':name,'category':category,'color':color, 'mrp':mrp},ignore_index=True)
        except:
            pass
        
df.to_csv(r"C:\Users\navaneethangn\Desktop\Nike_men_shoes.csv")
        
