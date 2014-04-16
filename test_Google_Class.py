__author__ = 'Hanqing'
from Google_Class import Google_Class


def main():
    my_key = 'AIzaSyDgcTb1_X2e-FZxsluhEdV-TRMAioOrjW8'
    my_id = '009400449333405283817:aefsx9jwd50'
    test_class = Google_Class(my_key, my_id, 10)
    query = "Seward Zheng"
    test_class.search(query)
    test_class.print_result()


if __name__ == '__main__':
    main()
