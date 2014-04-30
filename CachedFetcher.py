from BingService import BingService
from FacebookService import FacebookService
from GoogleService import GoogleService
from TwitterService import TwitterService
from LinkedInService import LinkedInService
from CrawlingNERService import CrawlingNERService
from BingCounterService import BingCounterService
from CrawlerService import CrawlerService
from myner import MyNER
import cPickle as pickle



class CachedFetcher(object):

    def __init__(self):
        try:
            self.cache = pickle.load(open("cache.dat", "r"))
        except IOError:
            self.cache = {}
        tagger = MyNER("localhost", 1234)
        fb_service = FacebookService('doubi670@gmail.com', 'wobushidoubi')
        crawl_service = CrawlerService(self.cache, fb_service)
        self.crawlers = {"bing":  BingService("LBgs97jt04iG6VUNDzHQUMoXPpHxCThQMIZ1sRGR9HI", 10),
            "bingct": BingCounterService(),
            "fb": fb_service,
            "goog": GoogleService("AIzaSyDgcTb1_X2e-FZxsluhEdV-TRMAioOrjW8", "009400449333405283817:aefsx9jwd50", 10),
            "twtr": TwitterService("323861641-2QMc92Bg6jV7dDUYPg3yvSJmhRCpEJncvq0rGZzn", "soso40fYcGP9G4pr9fYj6GjSLVV0ny50KDJwBgiOrDcPO", "7G5CoXNtxP6XbfgTSyNzzA", "98Upsqkir4vz5PAsRjwSyrkKwDGSB2QB4rI6dNXnAk", 20, tagger),
            "lkin": LinkedInService(),
            "ner": CrawlingNERService(tagger, crawl_service),
            "http": crawl_service}

    def crawl(self, engine, query):
        if engine in self.cache and query in self.cache[engine]:
            return self.cache[engine][query]
        result = self.crawlers[engine].search(query)
        if engine not in self.cache:
            self.cache[engine] = {}
        if not (engine == "bingct" and result == -1L):
            self.cache[engine][query] = result
        return result

    def persist(self):
        pickle.dump(self.cache, open("cache.dat", "w"))
