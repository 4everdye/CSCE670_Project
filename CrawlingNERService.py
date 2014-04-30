__author__ = 'Seward'
from bs4 import BeautifulSoup


class CrawlingNERService(object):
    def __init__(self, tagger, crawler):
        self.tagger = tagger
        self.crawler = crawler

    def ner(self, text):
        soup = BeautifulSoup(text)
        for tag in soup.find_all('script'):
            tag.replaceWith('')
        text = soup.get_text()
        return self.tagger.ner(text)

    def search(self, url):
        return self.ner(self.crawler.search(url))
