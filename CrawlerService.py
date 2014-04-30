__author__ = 'Seward'
import requests


class CrawlerService(object):

    def __init__(self, cache, fb_service):
        self.cache = cache
        self.fb_service = fb_service

    def search(self, url):
        if (not url.startswith("http")) or url.endswith(".pdf"):
            return ' '
        if "http" not in self.cache:
            self.cache["http"] = {}
        if url in self.cache["http"]:
            return self.cache["http"][url]
        elif "//m.facebook.com" in url:
            page = self.fb_service.fetch(url)
        else:
            page = requests.get(url).content
        if page:
            self.cache["http"][url] = page
        return unicode(page, errors='ignore').encode("ascii", "ignore")
