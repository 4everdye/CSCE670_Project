__author__ = 'Seward'
from CrawlerService import CrawlerService
from myner import MyNER
from bs4 import BeautifulSoup


def main():
    url = 'https://parasol.tamu.edu/~bs/'
    test_class = CrawlerService({}, None)
    tagger = MyNER("localhost", 1234)
    text = test_class.search(url)
    soup = BeautifulSoup(text)
    for tag in soup.find_all('script'):
        tag.replaceWith('')
    text = soup.get_text()
    print text
    print tagger.ner(text)


if __name__ == '__main__':
    main()

