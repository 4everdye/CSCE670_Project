def dist_vector(a, b):
    ret = []
    for i in xrange(len(a)):
        ret.append(float(a[i] - b[i]))
    return ret


def normalize(data):
    if not data:
        return
    for i in xrange(len(data[0])):
        lb = 1e50
        ub = -1e50
        for j in data:
            lb = min(lb, j[i])
            ub = max(ub, j[i])
        if ub != lb:
            for j in data:
                j[i] = (j[i] - lb + 0.0) / (ub - lb)
