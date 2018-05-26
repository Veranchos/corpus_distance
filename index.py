from readers.txt_reader import read_txt
from readers.csv_reader import read_csv
from readers.words_reader import read_words
from spearman import compute_spearman
from corpus import normalize_corpora, create_vectors, relativization
from vectors import calculate_vectors_distance
from kilgarriff import compare_measurement, ksc_in_intervals, find_best_interval, compare_known_similarity_corpora
from chi_square import create_contingency_table, chi_square
from euclidean import euclidean
from manhattan import manhattan
import csv

corpus1 = read_words('words/SCO.csv')
corpus2 = read_words('words/GUA.csv')

# n_corpus1, n_corpus2 = normalize_corpora(corpus1, corpus2)

# path1 = "./results/TOD-SCO500/normalized_TOD.csv"
# path2 = "./results/TOD-SCO500/normalized_SCO.csv"
#
#
# with open(path1, "w", encoding='utf-8') as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows(n_corpus1)
#
# with open(path2, "w", encoding='utf-8') as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows(n_corpus2)



def compute_a_result(corpus1, corpus2, measurement):
    # best_n = find_best_interval(corpus1, corpus2, measurement)
    result = ksc_in_intervals(corpus1[:400000], corpus2[:400000], measurement, 400, 10)

    return result



print(compute_a_result(corpus2, corpus1, compute_spearman))

# csvfile = "./results/TOD-SCO500/spearman.csv"
# result = compute_a_result(n_corpus1, n_corpus2, compute_spearman) # 45571
#
# with open(csvfile, "w", encoding='utf-8') as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows(result)
#
# csvfile1 = "./results/TOD-SCO500/euclidean.csv"
# result1 = compute_a_result(n_corpus1, n_corpus2, euclidean)
#
# with open(csvfile1, "w", encoding='utf-8') as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows(result1)
#
# csvfile2 = "./results/TOD-SCO500/manhattan.csv"
# result2 = compute_a_result(n_corpus1, n_corpus2, manhattan)
#
# with open(csvfile2, "w", encoding='utf-8') as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows(result2)
#
# csvfile3 = "./results/TOD-SCO500/cosine.csv"
# result3 = compute_a_result(n_corpus1, n_corpus2, calculate_vectors_distance)
#
# with open(csvfile3, "w", encoding='utf-8') as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows(result3)
#
# csvfile4 = "./results/TOD-SCO500/chi_square.csv"
# result4 = compute_a_result(n_corpus1, n_corpus2, chi_square)
#
# with open(csvfile4, "w", encoding='utf-8') as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows(result4)
