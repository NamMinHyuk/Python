# -*- coding:utf-8 -*-

# pip install requests
from bs4 import BeautifulSoup
import requests
import json


url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=thu'

resp = requests.get(url)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

# 제목 [별점]

img_list = soup.find('ul' , class_= 'img_list')

webtoons = img_list.select('dl')
lst = list()
for webtoon in webtoons:
    title = webtoon.find('a')['title']
    star = webtoon.find('strong').text
    # print('{} [{}]'.format(title, star))
    tmp = {}
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)
    
# print(lst)
res = {}
res['webtoons'] = lst

res_json = json.dumps(res , ensure_ascii=False)
# print(res_json)

with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)