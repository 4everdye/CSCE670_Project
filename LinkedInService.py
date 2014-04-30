__author__ = 'Hanqing'
import requests
import re


class LinkedInService:
    First_Name = ""
    Last_Name = ""
    url = ""


    def search(self, query):
        name = query.split(' ')
        self.search_res = []
        if len(name) == 0:
            return self.search_res
        if len(name) == 1:
            self.First_Name = name[0]
        elif len(name) > 1:
            self.First_Name = name[0]
            self.Last_Name = name[-1]
        self.url = "https://www.linkedin.com/pub/dir/?first={}&last={}&search=Search".format(self.First_Name, self.Last_Name)
        page = requests.get(self.url)
        persons = re.findall(r'<.*?class="vcard.*?">.*?<h2>.*?<strong>.*?<a href="(.*?)" title="(.*?)">', page.content, re.DOTALL)
        for person in persons:
            if len(self.search_res) == 10:
                break
            self.search_res.append([person[1], person[0]])
        return self.search_res


    def print_result(self):
        for item in self.search_res:
            print item[0] + ': ' + item[1] + '\n'
