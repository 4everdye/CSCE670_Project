__author__ = 'Hanqing'
from LinkedIn_Class import LinkedIn_Class


def main():
    query = 'Hanqing Zhao'
    test_class = LinkedIn_Class()
    test_class.search(query)
    test_class.print_result()
    pass


if __name__ == '__main__':
    main()



