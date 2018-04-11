from csvReader import read_csv
from txt_reader import read_txt
from corpus import create_vectors, normalize_corpora, calculate_N
from vectors import compare_sub_vectors_distance, compare_vectors_distance, calculate_distance_between_vectors_in_interval, compare_vectors_distance_2, manhattan_distance
from kilgarriff import create_known_similarity_corpora, compare_known_similarity_corpora
from scipy import stats
#
# corpus1 = read_csv('written_medium_book.csv')
# corpus2 = read_csv('wl_2018-03-14_23_23_58.csv')
# corpus3 = read_csv('written_academic_medicine.csv')
# corpus4 = read_csv('written_fiction_poetry.csv')

corpus5 = read_txt('antconc_HP.txt')
corpus6 = read_txt('antconc_LOTR.txt')
#
# c3, c4 = normalize_corpora(corpus3, corpus4)
# c3, c4 = normalize_corpora(corpus3, corpus4)
c5, c6  = normalize_corpora(corpus5, corpus6)

# print(c5)
# print(c6)
#
# vector3, vector4 = create_vectors(c3, c4)
# # sub_vector_distance = compare_sub_vectors_distance(vector1, vector2, 100, 10)
#
# print(sub_vector_distance)
# print('full vector - ', compare_vectors_distance(vector1, vector2))
#
# corpora = create_known_similarity_corpora(c1, c2)
#
#
# def func(corpus1, corpus2):
#     vector1, vector2 = create_vectors(corpus1, corpus2)
#     # distance = compare_vectors_distance(vector1, vector2)
#     interval = len(vector1) // 10
#     distance = calculate_distance_between_vectors_in_interval(vector1, vector2, [100, len(vector1)])
#     return distance
#
#
# result = compare_known_similarity_corpora(corpora, func)
#
# print(result)

# for row in corpora:
#     print(row)
#
# print(compare_vectors_distance_2(vector3, vector4))
# print(compare_vectors_distance_2(vector3, vector3))
# print(compare_vectors_distance(vector3, vector4))
#
# vector = [(vector3[index] + vector4[index]) / 2 for index in range(len(vector4))]
# new_vector = [[vector3[index], vector4[index]] for index in range(len(vector4))]
#
# # print(vector)
# # print(vector3)
# # print(vector4)
#
# res = stats.chisquare([vector3, vector4])
# # res1 = stats.chisquare(new_vector, vector)
#
# print(res)


# print(calculate_N(c5))
c = []
for i in range(len(c5)):
    c.append([c5[i][0], c5[i][1] + c6[i][1]])
print(calculate_N(c))
print(len(c5), len(c6))