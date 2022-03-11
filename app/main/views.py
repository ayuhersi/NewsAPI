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
    
    for i in range(len(t_articles)):
        main_article = t_articles[i]
        
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        
        contents = zip( news,desc,img,p_date,url)
        
    for j in range(len(a_articles)): 
        main_all_articles = a_articles[j]    

        

    
    return render_template('index.html',contents=contents,all = all)

if __name__ =='__main__':
    app.run(debug=True) 



