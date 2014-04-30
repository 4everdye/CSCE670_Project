__author__ = 'Hanqing'
from LinkedInService import LinkedInService


def main():
    query = 'Hanqing Zhao'
    test_class = LinkedInService()
    test_class.search(query)
    test_class.print_result()
    pass


if __name__ == '__main__':
    main()



