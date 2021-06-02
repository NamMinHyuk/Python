# -*- coding:utf-8 -*-

# pip install beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(resp, 'html.parser')
# print(soup)

# movies 안에 있는 제목과 별점을 파싱해서
# 제목 [별점] 으로 반복해서 출력하자.

# list에 담아서 하는 방식
movies = soup.select('dt a')
stars = soup.select('div a span:nth-of-type(2)')

movie_list = list()
star_list = list()

for r in movies:
    movie_list.append(r.text)
for r in stars:
    star_list.append(r.text)


# 바로 출력
movies_1 = soup.find_all('dl' , class_ = 'lst_dsc')

for movie in movies_1:
    title = movie.find('a').text
    star = movie.find('span', class_='num').text
    print('{} [{}]'.format(title, star))


