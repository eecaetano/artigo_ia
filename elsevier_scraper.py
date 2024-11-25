import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API da Elsevier do arquivo .env
ELSEVIER_API_KEY = os.getenv('ELSEVIER_API_KEY')

def fetch_elsevier_articles(query):
    headers = {
        'X-ELS-APIKey': ELSEVIER_API_KEY
    }
    url = f"https://api.elsevier.com/content/search/scidir?query={query}"
    response = requests.get(url, headers=headers)
    data = response.json()
    articles = []

    for entry in data['search-results']['entry']:
        title = entry['dc:title']
        link = entry['prism:url']
        articles.append({'title': title, 'link': link})

    return articles
