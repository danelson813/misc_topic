import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import re
import sqlite3 as sql
from sql_helper import *


def fix_rank(str_):
    text = str_
    temp = re.findall(f"\d+", text)
    return temp[0]

url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# print(soup)

# with open('page.txt', 'w') as f:
#     f.write(page.text)
# with open('page.txt', 'r') as f:
#     page = f.read()
# if page:
#     print('loaded ok')
# soup = bs(page, 'html.parser')
movies = soup.find('tbody').find_all('tr')
data = []
for movie in movies:
    results = {}
    title = movie.find("td", class_='titleColumn').find('a').text
    year = movie.find("td", class_='titleColumn').find('span').text
    rank = movie.find("td", class_='titleColumn').find('div', class_='velocity').text
    results = {
        'rank': fix_rank(rank),
        'title': title,
        'year': year[1:5],
    }
    data.append(results)

df = pd.DataFrame(data)
# df.to_csv('DATA.csv', index=False)

conn = sql.connect('popular_movies.db')
# df.to_sql('popular_movies', conn)


conn = sql.connect('popular_movies.db')
cur = conn.cursor()
# res = cur.execute("""SELECT * FROM popular_movies;""")
# conn.commit()
# print(res.fetchall())  # can be fetchall fetchone or fetchmany

res = cur.execute(select_one)
print(res.fetchone())

# res = cur.execute(select_all)
# print(res.fetchall())
