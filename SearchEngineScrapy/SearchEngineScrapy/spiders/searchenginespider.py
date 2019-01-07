from scrapy.selector import Selector
from scrapy.spider import Spider

from SearchEngineScrapy.utils.searchengines import SearchEngineResultSelector
from SearchEngineScrapy.utils.searchenginepages import SearchEngineURLs

import requests

class SearchEngineScrapy(Spider):
    name = "SearchEngineScrapy"

    allowed_domains = ['bing.com','google.com']
    start_urls = []

    searchQuery = None
    searchEngine = None
    fileType = None
    selector = None

    def __init__(self, searchQuery, fileType, searchEngine = "bing", pages = 3, *args, **kwargs):
        super(SearchEngineScrapy, self).__init__(*args, **kwargs)
        self.searchQuery = searchQuery.lower()
        self.fileType = fileType.lower()
        if fileType is not None:
            self.searchQuery = "{0} filetype:{1}".format(self.searchQuery, self.fileType)
        self.searchEngine = searchEngine.lower()
        self.pages = int(pages)

        pageUrls = SearchEngineURLs(self.searchQuery, self.searchEngine, self.pages)
        self.selector = SearchEngineResultSelector[self.searchEngine]

        for url in pageUrls:
            self.start_urls.append(url)

    def is_filetype(self, fileType, urlInfo):
        fileType_dict = {
            'pdf': 'application/pdf',
            'csv': 'text/csv',
            'zip': 'application/zip',
            'doc': 'application/msword',
            'docx': 'application/msword',
            'jpeg': 'image/jpeg',
            'png': 'image/png'
        }
        if urlInfo.headers['content-type'] == fileType_dict[fileType]:
            return True
        else:
            False
    
    def parse(self, response):
        for url in Selector(response).xpath(self.selector).extract():
            if self.searchEngine == "google":
                url = "https://www.google.com{}".format(url)
            urlInfo = requests.head(url, allow_redirects=True)
            url = urlInfo.url
            if self.is_filetype(self.fileType, urlInfo):
                yield { 'url': url }
        
        pass