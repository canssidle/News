class Source:
    """
    Source class to define news object
    """

    def __init__(self, id, name,description,url):

        self.id = id
        self.name = name
        self.description = description
        self.url = url
        
          


# class Article:
#     all_articles = []

#     def __init__(self, author, title, description, urlToImage, publishedAt, content):
#         self.id = author
#         self.title = title
#         self.description = description
#         self.urlToImage = urlToImage
#         self.publishedAt = publishedAt
#         self.content = content