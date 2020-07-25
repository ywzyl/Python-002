import requests
from bs4 import BeautifulSoup as bs

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

header = {'user-agent':user_agent}

url = "https://maoyan.com/films?showType=3"

# res = requests.get(url=url, headers=header)


with open('res', 'r', encoding='utf-8') as f:
    res = f.read()

bs_info = bs(res, 'html.parser')

# 找到所有电影信息
films_content = [tags.text for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'})]

# 取出前十条电影信息
films_ten = []
for j in range(0,10):
    films_target = list(filter(None, films_content[j].split('\n')))
    film = list(filter(None, [i.strip() for i in films_target]))
    del film[1:3]
    del film[2:5]
    films_ten.append(film)


import pandas as pd

movie1 = pd.DataFrame(data = films_ten)

movie1.to_csv('movie1.csv', encoding='utf8', index=False, header=False)

