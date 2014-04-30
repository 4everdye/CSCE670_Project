__author__ = 'Seward'

from sklearn import svm
from Main import compute_features
from Main import manual_ranker
from Utils import normalize
from Utils import dist_vector
import cPickle as pickle


input_list = ["TheRealCaverlee", "stroustrup", "choe@tamu.edu"]


def generate_diff_data(entities, person_mat, org_mat, loc_mat):
    person_result, org_result, loc_result = manual_ranker(entities, person_mat, org_mat, loc_mat)
    data_pair = [("PERSON", person_mat, person_result), ("ORGANIZATION", org_mat, org_result), ("LOCATION", loc_mat, loc_result)]
    ret = []
    for type, mat, result in data_pair:
        print "\n\nShowing", type
        for i in result:
            print "%d: %s" % (i, entities[type][i][0])
        remainder = set(result)
        layers = []
        while True:
            res = raw_input("Good results:")
            if not res:
                break
            res_str = res.split()
            res = set()
            for num in res_str:
                res.add(int(num))
            layers.append(res)
            remainder -= res
        layers.append(remainder)
        Xs, ys = [], []
        for i in xrange(len(layers) - 1):
            for j in xrange(i + 1, len(layers)):
                for a in layers[i]:
                    for b in layers[j]:
                        Xs.append(dist_vector(mat[a], mat[b]))
                        ys.append(1)
                        Xs.append(dist_vector(mat[b], mat[a]))
                        ys.append(-1)
        ret.append((Xs, ys))
    return ret


def training_error(X, y, clf):
    er, sum = 0.0, 0
    for i in xrange(len(X)):
        if clf.predict(X[i]) != [y[i]]:
            er += 1
        sum += 1
    return er / sum


def main():
    X_person, y_person = [], []
    X_org, y_org = [], []
    X_loc, y_loc = [], []
    for input in input_list:
        entities, person_mat, org_mat, loc_mat = compute_features(input)
        normalize(person_mat)
        normalize(org_mat)
        normalize(loc_mat)
        Xys = generate_diff_data(entities, person_mat, org_mat, loc_mat)
        X_person += Xys[0][0]
        y_person += Xys[0][1]
        X_org += Xys[1][0]
        y_org += Xys[1][1]
        X_loc += Xys[2][0]
        y_loc += Xys[2][1]

    print "Training Person Ranks..."
    clf_person = svm.SVC(C=1, kernel='linear')
    clf_person.fit(X_person, y_person)
    print "Training Error = %.2f%%" % (training_error(X_person, y_person, clf_person) * 100)
    print "Training Organization Ranks..."
    clf_org = svm.SVC(C=1, kernel='linear')
    clf_org.fit(X_org, y_org)
    print "Training Error = %.2f%%" % (training_error(X_org, y_org, clf_org) * 100)
    print "Training Location Ranks..."
    clf_loc = svm.SVC(C=1, kernel='linear')
    clf_loc.fit(X_loc, y_loc)
    print "Training Error = %.2f%%" % (training_error(X_loc, y_loc, clf_loc) * 100)
    print "Storing Classifiers..."
    pickle.dump((clf_person, clf_org, clf_loc), open("classifiers.dat", "w"))


if __name__ == "__main__":
    main()
