# scrapers/scielo_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_scielo_articles(query):
    url = f"https://search.scielo.org/?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for item in soup.find_all('div', class_='item'):
        title = item.find('a', class_='title').text
        link = item.find('a', class_='title')['href']
        articles.append({'title': title, 'link': link})

    return articles
