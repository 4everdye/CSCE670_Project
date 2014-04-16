__author__ = 'Hanqing'
from Bing_Class import Bing_Class
import sys


def main():
    query = ""
    my_key = "LBgs97jt04iG6VUNDzHQUMoXPpHxCThQMIZ1sRGR9HI"
    test_class = Bing_Class(my_key, "Web", "json", 10)
    while not query == "esc":
        query = raw_input("Please input query:\n")
        if query == "esc":
            break
        Search_res = test_class.search(query)
        for item in Search_res:
            print item + ': \n' + Search_res[item][0] + '\n' + Search_res[item][1] + '\n'
    sys.exit(1)

if __name__ == "__main__":
    main()
