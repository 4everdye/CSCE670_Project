import tweepy


class Twitter_Class:
    access_token = "323861641-2QMc92Bg6jV7dDUYPg3yvSJmhRCpEJncvq0rGZzn"
    access_token_secret = "soso40fYcGP9G4pr9fYj6GjSLVV0ny50KDJwBgiOrDcPO"
    consumer_key = "7G5CoXNtxP6XbfgTSyNzzA"
    consumer_secret = "98Upsqkir4vz5PAsRjwSyrkKwDGSB2QB4rI6dNXnAk"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    limit = None
    search_res = []
        
    def __init__(self, token, token_secret, consumer_key, consumer_secret, limit):
        self.access_token = token
        self.access_token_secret = token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.limit = limit

    def search(self, query):
        for tweet in tweepy.Cursor(self.api.search, q=query, result_type="recent", include_entities=True, lang="en").items(self.limit):
            self.search_res.append([tweet.author.screen_name.encode('utf-8'), tweet.text.encode('utf-8')])
        return self.search_res

    def print_result(self):
        for tweet in self.search_res:
            print tweet[0] + '\n' + tweet[1] + '\n'
