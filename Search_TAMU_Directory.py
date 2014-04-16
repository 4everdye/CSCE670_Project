__author__ = 'Hanqing'
import requests
import re


def search_directory(query):
    url_pre = "https://services.tamu.edu/directory-search/?branch=people&cn="
    url = url_pre + query
    page = requests.get(url)
    content = page.content
    print content
    links = re.findall(r'<a href="(/directory-search/people/.*?)"', content)
    attrs = ['Name', 'Major', 'Local Phone', 'Email Address']
    for link in links:
        personal_page_url = "https://services.tamu.edu" + link
        personal_page = requests.get(personal_page_url)
        personal_info = personal_page.content
        person_dict = get_info(personal_info)
        for attr in attrs:
            if attr in person_dict:
                print attr + ': '+ person_dict[attr]
    return


def get_info(personal_info):
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


def main():
    query = "Shihua Zheng"
    search_directory(query)


if __name__ == '__main__':
    main()
