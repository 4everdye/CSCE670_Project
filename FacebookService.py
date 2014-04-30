__author__ = 'Hanqing'
import urllib2
import urllib
import cookielib
import re


class FacebookService(object):
    jar = cookielib.CookieJar()
    cookie = urllib2.HTTPCookieProcessor(jar)
    opener = urllib2.build_opener(cookie)
    email = 'doubi670@gmail.com'
    password = 'wobushidoubi'
    search_res = []

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14",
        "Accept": "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Charset": "ISO-8859-1",
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "m.facebook.com"
    }
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.need_login = True

    def login(self):
        try:
            params = urllib.urlencode({'email': self.email, 'pass': self.password, 'login': 'Log+In'})
            req = urllib2.Request('http://m.facebook.com/login.php?m=m&refsrc=m.facebook.com%2F', params, self.headers)
            res = self.opener.open(req)
            self.need_login = False
        except urllib2.HTTPError, e:
            print e.msg
        except urllib2.URLError, e:
            print e.reason[1]
        return False

    def fetch(self, url):
        req = urllib2.Request(url, None, self.headers)
        res = self.opener.open(req)
        return res.read()

    def search(self, query):
        if self.need_login:
            self.login()
        self.search_res = []
        query = urllib.quote_plus(query)
        url = "https://m.facebook.com/findfriends/search/?refid=7&ref=wizard&q=" + query + "&submit=Search"
        page = self.fetch(url)
        persons = re.findall(r'<tr>.*?<td class="name">.*?<a href="(.*?)">.*?<span class="mfsm">(.*?)</span>.*?</tr>', page)
        for person in persons:
            self.search_res.append([person[1], 'https://m.facebook.com' + person[0]])
            # self.search_res[person[1]] = 'm.facebook.com' + person[0]
        return self.search_res

    def print_result(self):
        for item in self.search_res:
            print item[0] + ': ' + item[1] + '\n'
