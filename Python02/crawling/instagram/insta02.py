# -*- coding:utf-8 -*-

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')

driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')

for imgs in img_list:
    print(imgs.img['src'])
driver.close()
driver.quit()