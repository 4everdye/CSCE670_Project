__author__ = 'Hanqing'
import requests
import urllib


class Bing_Class:
    search_url = ""
    my_key = ""
    type = ""
    format = ""
    limit = ""

    def __init__(self, key, type, format, limit):
        self.my_key = key
        self.type = type
        self.format = format
        self.limit = limit

    def form_url(self, query):
        url_0 = "https://user:"
        url_1 = "@api.datamarket.azure.com/Bing/Search/"
        url_2 = "?Query="
        url_3 = "&$format="
        url_4 = "&$top="
        query = "'" + query + "'"
        query = urllib.quote_plus(query)
        self.search_url = url_0 + self.my_key + url_1 + self.type + url_2 + query + url_3 + self.format + url_4 + str(self.limit)

    def search(self, query):
        self.form_url(query)
        page = requests.get(self.search_url)
        page_dict = page.json()
        Search_res = {}
        for issue in page_dict['d']['results']:
            Search_res[issue['Title'].encode('utf-8')] = [issue['Description'].encode('utf-8'), issue['DisplayUrl'].encode('utf-8')]
        return Search_res
