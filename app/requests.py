import urllib.request,json
from .models import Source,Article




# getting api key 
api_key = None

# getting the news based url 
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    """
    function that gets the json response to our url request
    """
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url :
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = []

        if get_news_response["sources"]:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results





def process_results(news_list):

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
       
              
        news_object = Source(id, name,description,url)
        news_results.append(news_object)

    return news_results