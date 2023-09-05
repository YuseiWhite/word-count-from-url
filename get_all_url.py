import requests
from bs4 import BeautifulSoup

# ここにサイトツリーの取得したいページを貼ってください
url = "https://move-language.github.io/move/print.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# devタグ "sidebar-scrollbox" クラス以下のリストになっているURLを取得する 
links = soup.select('ol.chapter li a')

# href属性のみを取得してリストに格納
urls = [link.get('href') for link in links if link.get('href')]

# URLのベース
base_url = "https://move-language.github.io/move/"

# 完全なURLに変換
full_urls = [base_url + link for link in urls]

# テキストファイルに保存
with open('urls.txt', 'w') as file:
    for url in full_urls:
        file.write(url + '\n')
