import tweepy


class TwitterService(object):
    access_token = "323861641-2QMc92Bg6jV7dDUYPg3yvSJmhRCpEJncvq0rGZzn"
    access_token_secret = "soso40fYcGP9G4pr9fYj6GjSLVV0ny50KDJwBgiOrDcPO"
    consumer_key = "7G5CoXNtxP6XbfgTSyNzzA"
    consumer_secret = "98Upsqkir4vz5PAsRjwSyrkKwDGSB2QB4rI6dNXnAk"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    limit = None
    search_res = []
        
    def __init__(self, token, token_secret, consumer_key, consumer_secret, limit, tagger):
        self.access_token = token
        self.access_token_secret = token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.limit = limit
        self.tagger = tagger

    def search(self, query):
        str = ''
        for tweet in tweepy.Cursor(self.api.search, q=query, result_type="mixed", include_entities=True, lang="en").items(self.limit):
            str += tweet.author.screen_name.encode("ascii", "ignore") + ", " + tweet.text.encode("ascii", "ignore")
        return self.tagger.ner(str)

    def print_result(self):
        for tweet in self.search_res:
            print tweet[0] + '\n' + tweet[1] + '\n'
