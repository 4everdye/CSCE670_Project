__author__ = 'Hanqing'
import requests
import urllib


class Google_Class:
    my_key = 'AIzaSyDgcTb1_X2e-FZxsluhEdV-TRMAioOrjW8'
    my_id = '009400449333405283817:aefsx9jwd50'
    url = ""
    limit = None
    search_res = []
    
    def __init__(self, limit):
        self.limit = limit

    def __init__(self, key, id, limit):
        self.my_key = key
        self.my_id = id
        self.limit = limit

    def search(self, query):
        self.url = 'https://www.googleapis.com/customsearch/v1?key={}&cx={}&alt=json&q={}&num={}'.format(self.my_key, self.my_id,urllib.quote_plus(query), self.limit)
        result = requests.get(self.url)
        result_json = result.json()
        for item in result_json['items']:
            self.search_res.append([item['title'].encode('utf-8'), item['snippet'].encode('utf-8'), item['link'].encode('utf-8')])
        return self.search_res

    def print_result(self):
        for item in self.search_res:
            print item[0] + ': \n' + item[1] + '\n' + item[2] + '\n'
