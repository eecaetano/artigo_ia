# scrapers/science_gov_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_science_gov_articles(query):
    url = f"https://www.science.gov/search?query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for item in soup.find_all('h3', class_='result-title'):
        title = item.text
        link = item.find('a')['href']
        articles.append({'title': title, 'link': link})

    return articles
