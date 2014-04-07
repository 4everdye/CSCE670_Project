__author__ = 'Hanqing'
import requests
import string


def Bing_search(key, type, query, format, limit):
    url_0 = "https://user:"
    url_1 = "@api.datamarket.azure.com/Bing/Search/"
    url_2 = "?Query="
    url_3 = "&$format="
    url_4 = "&$top="
    query = "\"" + query + "\""
    query = string.replace(query, "'", '%27')
    query = string.replace(query, '"', '%27')
    query = string.replace(query, '+', '%2b')
    query = string.replace(query, ' ', '%20')
    query = string.replace(query, ':', '%3a')
    url = url_0 + key + url_1 + type + url_2 + query + url_3 + format + url_4 + str(limit)
    return url


def Bing_search_2(key, query, source, limit):
    url_0 = "http://api.bing.net/json.aspx?AppId= "
    url_1 = "&Version=2.2&Market=en-US&Query="
    url_2 = "&Sources="
    url_3 = "&Web.Count= "
    query = "\""+query+"\""
    query = string.replace(query, "'", '%27')
    query = string.replace(query, '"', '%27')
    query = string.replace(query, '+', '%2b')
    query = string.replace(query, ' ', '%20')
    query = string.replace(query, ':', '%3a')
    url = url_0 + key + url_1 + query + url_2 + source + url_3 + str(limit)
    return url


def main():
    my_key = "LBgs97jt04iG6VUNDzHQUMoXPpHxCThQMIZ1sRGR9HI"
    my_key_2 = "sPTc8a9IBhEDHaIs3mMUHJbvJJ6fU8tDu0/NWmIEHH4="

    url = Bing_search(my_key, "Web", "texas san antonio view", "json", 10)
    url_2 = Bing_search_2(my_key, "texas san antonio view", "web", 10)
    print url
    print url_2
    r = requests.get(url)
    r_dict = r.json()
    print r.status_code
    print r.headers['content-type']
    print r.encoding
    print r.text
    # print r.json()
    return


if __name__ == "__main__":
    main()
