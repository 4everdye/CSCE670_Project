__author__ = 'Hanqing'
from DirectoryService import DirectoryService


def main():
    test_class = DirectoryService()
    test_class.search("Shihua Zheng")
    test_class.print_result()


if __name__ == "__main__":
    main()
