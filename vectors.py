from scipy import spatial


def compare_vectors_distance(vector1, vector2):
    return spatial.distance.cosine(vector1, vector2)


def calculate_distance_between_vectors_in_interval(vector1, vector2, interval):
    interval_start, interval_end = interval

    sub_vector1 = vector1[interval_start: interval_end]
    sub_vector2 = vector2[interval_start: interval_end]
    return compare_vectors_distance(sub_vector1, sub_vector2)


def compare_sub_vectors_distance(vector1, vector2, interval, step):
    iterations = (len(vector1) - interval) // step
    distance_list = []

    for i in range(iterations):
        distance = calculate_distance_between_vectors_in_interval(vector1, vector2, [i * step, interval + i * step])
        distance_list.append(distance)

    return distance_list
