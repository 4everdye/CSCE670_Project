__author__ = 'Hanqing'
from test_bing import Bing_search
import sys
import requests


def main():
    query = ""
    my_key = "LBgs97jt04iG6VUNDzHQUMoXPpHxCThQMIZ1sRGR9HI"
    while not query == "esc":
        query = raw_input("Please input query:\n")
        url = Bing_search(my_key, "Web", query, "json", 10)
        r = requests.get(url)
        r_dict = r.json()
        Search_res = open(query+'.txt', 'w+')
        for issue in r_dict['d']['results']:
            Search_res.write(issue['Title'].encode('utf-8'))
            Search_res.write('\n')
            Search_res.write(issue['Description'].encode('utf-8'))
            Search_res.write('\n')
            Search_res.write(issue['DisplayUrl'].encode('utf-8'))
            Search_res.write('\n\n')
        Search_res.close()
    sys.exit(1)

if __name__ == "__main__":
    main()
