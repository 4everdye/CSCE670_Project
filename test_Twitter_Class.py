__author__ = 'Hanqing'
from TwitterService import TwitterService


def main():
    access_token = "323861641-2QMc92Bg6jV7dDUYPg3yvSJmhRCpEJncvq0rGZzn"
    access_token_secret = "soso40fYcGP9G4pr9fYj6GjSLVV0ny50KDJwBgiOrDcPO"
    consumer_key = "7G5CoXNtxP6XbfgTSyNzzA"
    consumer_secret = "98Upsqkir4vz5PAsRjwSyrkKwDGSB2QB4rI6dNXnAk"
    test_class = TwitterService(access_token, access_token_secret, consumer_key, consumer_secret, 20)
    query = "obama"
    test_class.search(query)
    test_class.print_result()


if __name__ == '__main__':
    main()
