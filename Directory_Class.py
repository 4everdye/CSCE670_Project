__author__ = 'Hanqing'
import requests
import re


class Directory_Class:
    attrs = ['Name', 'Major', 'Local Phone', 'Email Address']
    search_res = []

    def search(self, query):
        url_pre = "https://services.tamu.edu/directory-search/?branch=people&cn="
        url = url_pre + query
        page = requests.get(url)
        # print page.content
        links = re.findall(r'<a href="(/directory-search/people/.*?)"', page.content)
        for link in links:
            personal_page_url = "https://services.tamu.edu" + link
            personal_page = requests.get(personal_page_url)
            # personal_info = personal_page.content
            person_dict = self.get_info(personal_page.content)
            self.search_res.append(person_dict)
        return self.search_res

    def get_info(self, personal_info):
        res = {}
        titles = re.findall(r'<th>(.*?):</th>', personal_info)
        issues = re.findall(r'<td>(.*?)</td>', personal_info)
        for i in xrange(len(titles)):
            title = titles[i]
            issue = issues[i]
            if title == 'Email Address':
                email = re.findall(r'mailto:(.*?)"', issue)[0]
                res[title] = email
            elif title == 'Classification':
                continue
            else:
                res[title] = issue
        return res

    def print_result(self):
        for person_dict in self.Search_res:
            for attr in self.attrs:
                if attr in person_dict:
                    print attr + ': ' + person_dict[attr]
