__author__ = 'Hanqing'
import urllib2
import urllib
import cookielib
import re


class Facebook_Class:
    jar = cookielib.CookieJar()
    cookie = urllib2.HTTPCookieProcessor(jar)
    opener = urllib2.build_opener(cookie)

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14",
        "Accept": "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Charset": "ISO-8859-1",
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "m.facebook.com"
    }
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #     "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    #     "Accept-Charset": "ISO-8859-1",
    #     "Content-type": "text/html; charset=utf-8",
    #     "Host": "m.facebook.com"
    # }

    def login(self):
        try:
            params = urllib.urlencode({'email': 'doubi670@gmail.com', 'pass': 'wobushidoubi', 'login': 'Log+In'})
            req = urllib2.Request('http://m.facebook.com/login.php?m=m&refsrc=m.facebook.com%2F', params, self.headers)
            res = self.opener.open(req)
            # html = res.read()
            # print html

            #print res.getheader('location').split('/')[3]

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
        query = urllib.quote_plus(query)
        url = "https://m.facebook.com/findfriends/search/?refid=7&ref=wizard&q=" + query + "&submit=Search"
        page = self.fetch(url)
        persons = re.findall(r'<tr>.*?<a href="(.*?)">.*?<span class="mfsm">(.*?)</span>.*?</tr>', page)
        res_person = {}
        for person in persons:
            res_person[person[1]] = 'm.facebook.com' + person[0]
        # print res_person
        return res_person


def main():
    test_class = Facebook_Class()
    test_class.login()
    search_res = test_class.search("Seward Zheng")
    for item in search_res:
        print item + ': ' + search_res[item] + '\n'

if __name__ == '__main__':
    main()
