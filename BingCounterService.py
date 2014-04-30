__author__ = 'Seward'

import requests
import urllib
import re


class BingCounterService(object):
    pattern = re.compile(r'<span class="sb_count">(.*?)</span>')
    num_ptn = re.compile("[0-9]")

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14",
        "Accept": "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Charset": "ISO-8859-1",
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "www.bing.com"
    }

    def search(self, query):
        url_pre = "http://www.bing.com/search?q="
        url = url_pre + urllib.quote_plus(query)
        page = requests.get(url, headers=self.headers)
        if re.search('<h1>No results found for', page.content):
            return 0
        tag = re.search('<span class="sb_count">(.*?)</span>', page.content)
        if not tag:
            print page.content
            return -1L
        result_str = ""
        for digit in re.findall('[0-9]', tag.group(1)):
            result_str += digit
        if result_str == '':
            return -1L
        return long(result_str)

