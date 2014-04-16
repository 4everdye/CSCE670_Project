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
        test_class.search(query)
        test_class.print_result()
    sys.exit(1)

if __name__ == "__main__":
    main()
