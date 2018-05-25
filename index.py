from readers.txt_reader import read_txt
from readers.csv_reader import read_csv
from spearman import compute_spearman
from corpus import normalize_corpora, create_vectors, relativization
from vectors import calculate_vectors_distance
from kilgarriff import compare_measurement, ksc_in_intervals, find_best_interval
from chi_square import create_contingency_table, chi_square
from euclidean import euclidean
from manhattan import manhattan
import csv

corpus1 = read_csv('exported/TOD.csv')
corpus2 = read_csv('exported/SCO.csv')

n_corpus1, n_corpus2 = normalize_corpora(corpus1, corpus2)

def compute_a_result(corpus1, corpus2, measurement):
    best_n = find_best_interval(corpus1, corpus2, measurement)
    result = ksc_in_intervals(corpus1, corpus2, measurement, best_n, 10)

    return result

csvfile = "./results/TOD-SCO500/spearman.csv"
result = compute_a_result(n_corpus1, n_corpus2, compute_spearman) # 45571

with open(csvfile, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(result)

csvfile1 = "./results/TOD-SCO500/euclidean.csv"
result1 = compute_a_result(n_corpus1, n_corpus2, euclidean)

with open(csvfile1, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(result1)

csvfile2 = "./results/TOD-SCO500/manhattan.csv"
result2 = compute_a_result(n_corpus1, n_corpus2, manhattan)

with open(csvfile2, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(result2)

csvfile3 = "./results/TOD-SCO500/cosine.csv"
result3 = compute_a_result(n_corpus1, n_corpus2, calculate_vectors_distance)

with open(csvfile3, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(result3)

csvfile4 = "./results/TOD-SCO500/chi_square.csv"
result4 = compute_a_result(n_corpus1, n_corpus2, chi_square)

with open(csvfile4, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(result4)
