from bs4 import BeautifulSoup
import requests
import time

URL = 'https://movie.naver.com/movie/running/current.nhn'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'lxml')

movies = soup.select("ul.lst_detail_t1>li")

titles = []
search_titles = []

for movie in movies:
    titles.append(movie.find('dt', attrs={'class':'tit'}).a.get_text())
print()

while True:
    print('*'*30)
    print('현재 개봉 영화검색기')
    print("나가고 싶으시면 0을 눌러주세요")
    print('*'*30)
    search = input("영화 이름을 넣어주세요 : ")

    if search == '0':
        break

    for title in titles:
        if search in title:
            search_titles.append(title)
    print()
    if search_titles == []:
        print("찾는 영화가 없습니다")
    else:
        for title in search_titles:
            print(title)
    search_titles = []
    print()
    print()
    print()