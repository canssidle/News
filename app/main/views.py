from flask import render_template
from . import main
from ..requests import get_news
from ..models import Source, Article


#views
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    sources= get_news()
    
    

    title = "NEWS HIGLIGHTS"

    return render_template('index.html', title = title, sources=sources)






