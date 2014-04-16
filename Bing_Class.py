__author__ = 'Hanqing'
import requests
import urllib


class Bing_Class:
    search_url = ""
    my_key = ""
    type = "Web"
    format = "json"
    limit = ""
    search_res = []

    def __init__(self, key, limit):
        self.my_key = key
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
        for issue in page_dict['d']['results']:
            self.search_res.append([issue['Title'].encode('utf-8'), issue['Description'].encode('utf-8'), issue['Url'].encode('utf-8')])
        return self.search_res
        
    def print_result(self):
        for item in self.search_res:
            print item[0] + ': \n' + item[1] + '\n' + item[2] + '\n'
