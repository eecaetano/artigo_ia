# scrapers/scopus_scraper.py
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SCOPUS_API_KEY = os.getenv('SCOPUS_API_KEY')

def fetch_scopus_articles(query):
    headers = {
        'X-ELS-APIKey': SCOPUS_API_KEY
    }
    url = f"https://api.elsevier.com/content/search/scopus?query={query}"
    response = requests.get(url, headers=headers)
    data = response.json()
    articles = []

    for entry in data['search-results']['entry']:
        title = entry['dc:title']
        link = entry['prism:url']
        articles.append({'title': title, 'link': link})

    return articles
