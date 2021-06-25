import requests
from bs4 import BeautifulSoup

KEYWORDS = {'Научно-популярное', 'IT-компании', 'Программирование', 'Физика'}

response = requests.get('https://habr.com/ru/all/')
text = response.text

soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    hubs = {hub.text.strip() for hub in article.find_all('a', class_='hub-link')}
    if hubs & KEYWORDS:
        a = article.find('a', class_='post__title_link')
        time = article.find('span', class_='post__time')
        name = article.find('a', class_='post__title_link')
        print(f'<{time.text}>-<{name.text}>-<{a.attrs.get("href")}>')
