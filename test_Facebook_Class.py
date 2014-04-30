__author__ = 'Hanqing'
from FacebookService import FacebookService


def main():
    test_class = FacebookService('doubi670@gmail.com', 'wobushidoubi')
    test_class.login()
    test_class.search("Seward Zheng")
    test_class.print_result()
    test_class.search("James Caverlee")
    test_class.print_result()


if __name__ == '__main__':
    main()
