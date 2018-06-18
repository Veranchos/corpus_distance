from scipy.spatial import distance

def manhattan(corpus1, corpus2, interval):
    start, end = interval
    vector1 = [value for key, value in corpus1[start:end]]
    vector2 = [value for key, value in corpus2[start:end]]
    dist = distance.cityblock(vector1, vector2)
    return dist