from CachedFetcher import CachedFetcher
from collections import Counter
from Utils import normalize
from Utils import dist_vector
import cPickle as pickle
import math

service_name = {"bing": "Bing", "goog": "Google", "fb": "Facebook", "lkin": "LinkedIn", "twtr": "Twitter"}


def compute_features(query):
    fetcher = CachedFetcher()
    try:
        entities = {"ORGANIZATION": Counter(), "LOCATION": Counter(), "PERSON": Counter()}
        visited_urls = set()
        for i in ["bing", "goog"]:
            print "[Phase 1] Fetching", service_name[i], "..."
            for title, summary, url in fetcher.crawl(i, query):
                if url in visited_urls:
                    continue
                visited_urls.add(url)
                print "[Phase 1] Fetching", title, "@", url, "..."
                ner_results = fetcher.crawl("ner", url)
                print ner_results
                for type in ner_results:
                    entities[type] += Counter(filter(lambda x: len(x.split()) <= 10, ner_results[type]))
        fetcher.persist()
        print "[Phase 1] Fetching Twitter..."
        twtr_results = fetcher.crawl("twtr", query)
        for type in twtr_results:
            entities[type] += Counter(filter(lambda x: len(x.split()) <= 10, twtr_results[type]))
        for type in entities:
            print "[Phase 1] Observed", type, ":", len(entities[type])
        entities["PERSON"] = entities["PERSON"].most_common(50)
        entities["ORGANIZATION"] = entities["ORGANIZATION"].most_common(50)
        entities["LOCATION"] = entities["LOCATION"].most_common(50)
        person_mat = []
        loc_mat = []
        org_mat = []
        for i, count in entities["LOCATION"]:
            loc_mat.append([count, math.log(count + 1), 0])
        for i, count in entities["ORGANIZATION"]:
            org_mat.append([count, math.log(count + 1), 0])
        for i, count in entities["PERSON"]:
            name_set = set(i.lower().split())
            person_mat.append([count, math.log(count + 1), 1 / abs(len(name_set) - 2.5), 0])
            for j in ["fb", "lkin"]:
                print "[Phase 2] Fetching", service_name[j], "for name:", i
                for name, url in fetcher.crawl(j, i)[:5]:
                    snsname_set = set(name.lower().split())
                    if name_set >= snsname_set or snsname_set >= name_set:
                        results = fetcher.crawl("http", url).lower()
                        person_mat[-1][-1] += results.count(query.lower())
                        for k in xrange(len(entities["LOCATION"])):
                            loc_mat[k][2] += results.count(entities["LOCATION"][k][0].lower())
                        for k in xrange(len(entities["ORGANIZATION"])):
                            org_mat[k][2] += results.count(entities["ORGANIZATION"][k][0].lower())
            person_mat[-1].append(math.log(person_mat[-1][-1] + 1))
        for i in loc_mat:
            i.append(math.log(i[-1] + 1))
        for i in org_mat:
            i.append(math.log(i[-1] + 1))
        for i in xrange(len(entities["PERSON"])):
            name = entities["PERSON"][i][0]
            print "[Phase 2] Fetching Bing for name:", name
            results = fetcher.crawl("bingct", '"%s" "%s"' % (name, query))
            results = max(0, results)
            person_mat[i].append(results)
            person_mat[i].append(math.log(results + 1))
        for i in xrange(len(entities["LOCATION"])):
            name = entities["LOCATION"][i][0]
            print "[Phase 2] Fetching Bing for location:", name
            results = fetcher.crawl("bingct", '"%s" "%s"' % (query, name))
            results = max(0, results)
            loc_mat[i].append(results)
        for i in loc_mat:
            i.append(math.log(i[-1] + 1))
        for i in xrange(len(entities["ORGANIZATION"])):
            name = entities["ORGANIZATION"][i][0]
            print "[Phase 2] Fetching Bing for organization:", name
            results = fetcher.crawl("bingct", '"%s" "%s"' % (query, name))
            results = max(0, results)
            org_mat[i].append(results)
        for i in org_mat:
            i.append(math.log(i[-1] + 1))
        return entities, person_mat, org_mat, loc_mat
    finally:
        fetcher.persist()


def manual_ranker(entities, person_mat, org_mat, loc_mat):
    person_result = sorted(range(len(entities["PERSON"])), key=lambda i: -person_mat[i][5])
    org_result = sorted(range(len(entities["ORGANIZATION"])), key=lambda i: -org_mat[i][4])
    loc_result = sorted(range(len(entities["LOCATION"])), key=lambda i: -loc_mat[i][4])
    return person_result, org_result, loc_result


def ml_ranker(entities, person_mat, org_mat, loc_mat):
    clf_person, clf_org, clf_loc = pickle.load(open("classifiers.dat", "r"))
    data_set = [(person_mat, clf_person), (org_mat, clf_org), (loc_mat, clf_loc)]
    ret = []
    scores = []
    for data, clf in data_set:
        normalize(data)
        score = [0] * len(data)
        for i in xrange(len(data) - 1):
            for j in xrange(i + 1, len(data)):
                if clf.predict(dist_vector(data[i], data[j])) == [1]:
                    score[i] += 1
                else:
                    score[j] += 1
                if clf.predict(dist_vector(data[j], data[i])) == [-1]:
                    score[i] += 1
                else:
                    score[j] += 1
        result = sorted(range(len(data)), key=lambda i: -score[i])
        ret.append(result)
        scores.append(score)
    return ret, scores


def print_result(entities, person_result, org_result, loc_result, person_mat, org_mat, loc_mat):
    print "\n[RESULTS]"
    print "Person:"
    for i in xrange(min(len(person_result), 10)):
        print "Rank %d: %s (Score: %d)" % (i + 1, entities["PERSON"][person_result[i]][0], person_mat[person_result[i]])
    print "\nOrganization:"
    for i in xrange(min(len(org_result), 10)):
        print "Rank %d: %s (Score: %d)" % (i + 1, entities["ORGANIZATION"][org_result[i]][0], org_mat[org_result[i]])
    print "\nLocation:"
    for i in xrange(min(len(loc_result), 10)):
        print "Rank %d: %s (Score: %d)" % (i + 1, entities["LOCATION"][loc_result[i]][0], loc_mat[loc_result[i]])


def main():
    query = raw_input("Query (Name, ID or Email): ")
    entities, person_mat, org_mat, loc_mat = compute_features(query)
    #person_result, org_result, loc_result = manual_ranker(entities, person_mat, org_mat, loc_mat)
    results, scores = ml_ranker(entities, person_mat, org_mat, loc_mat)
    print_result(entities, results[0], results[1], results[2], scores[0], scores[1], scores[2])


if __name__ == "__main__":
    main()