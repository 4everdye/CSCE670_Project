__author__ = 'Hanqing'
from Facebook_Class import Facebook_Class


def main():
    test_class = Facebook_Class('doubi670@gmail.com', 'wobushidoubi')
    test_class.login()
    test_class.search("Seward Zheng")
    test_class.print_result()


if __name__ == '__main__':
    main()
