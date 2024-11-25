# scrapers/bdtd_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_bdtd_articles(query):
    url = f"http://bdtd.ibict.br/vufind/?search_type=all&query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for item in soup.find_all('div', class_='result'):
        title = item.find('a').text
        link = item.find('a')['href']
        articles.append({'title': title, 'link': link})

    return articles
