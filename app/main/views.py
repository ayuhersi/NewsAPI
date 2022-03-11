from flask import render_template
from flask import Flask
from newsapi import NewsApiClient
# Views

app = Flask(__name__)
@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='6c96ed5a47684e6aa3f87640d6945895')
    top_headlines = newsapi.get_top_headlines(sources="bbc-news")
    all_articles = newsapi.get_everything(sources="bbc-news")
    
    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']
    
    news = []
    desc = []
    img = []
    p_date = []
    url = []
    
    
    
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True) 



