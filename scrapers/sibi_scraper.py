# scrapers/sibi_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_sibi_articles(query):
    url = f"https://sibi.ufrj.br/?s={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for item in soup.find_all('div', class_='post-content'):
        title = item.find('h2').text
        link = item.find('a')['href']
        articles.append({'title': title, 'link': link})

    return articles
