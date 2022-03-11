from flask import render_template
from flask import Flask
from newsapi import NewsApiClient
# Views

app = Flask(__name__)
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True) 


    
