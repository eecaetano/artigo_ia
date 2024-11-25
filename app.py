# app.py
from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline
from scrapers.scielo_scraper import fetch_scielo_articles
from scrapers.scopus_scraper import fetch_scopus_articles
from scrapers.science_direct_scraper import fetch_science_direct_articles
from scrapers.bdtd_scraper import fetch_bdtd_articles
from scrapers.sibi_scraper import fetch_sibi_articles
from scrapers.science_gov_scraper import fetch_science_gov_articles
from scrapers.world_wide_science_scraper import fetch_world_wide_science_articles
from scrapers.scholarpedia_scraper import fetch_scholarpedia_articles

app = Flask(__name__)

selected_articles = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    scielo_articles = fetch_scielo_articles(query)
    scopus_articles = fetch_scopus_articles(query)
    science_direct_articles = fetch_science_direct_articles(query)
    bdtd_articles = fetch_bdtd_articles(query)
    sibi_articles = fetch_sibi_articles(query)
    science_gov_articles = fetch_science_gov_articles(query)
    world_wide_science_articles = fetch_world_wide_science_articles(query)
    scholarpedia_articles = fetch_scholarpedia_articles(query)
    
    articles = (scielo_articles + scopus_articles + science_direct_articles + bdtd_articles + 
                sibi_articles + science_gov_articles + world_wide_science_articles + scholarpedia_articles)
                
    return render_template('result.html', articles=articles, query=query)

@app.route('/select_articles', methods=['POST'])
def select_articles():
    global selected_articles
    selected_articles = request.form.getlist('articles')
    return redirect(url_for('generate_article'))

@app.route('/generate_article')
def generate_article():
    summarizer = pipeline("summarization")
    generated_article = "Artigo gerado com base nos artigos selecionados:\n"
    
    for article_url in selected_articles:
        response = requests.get(article_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_text = soup.get_text()
        summary = summarizer(article_text, max_length=100, min_length=30, do_sample=False)
        generated_article += f"{summary[0]['summary_text']}\n\n"

    return render_template('generated_article.html', article=generated_article)

if __name__ == '__main__':
    app.run(debug=True)
