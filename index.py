from readers.txt_reader import read_txt
from readers.csv_reader import read_csv
from spearman import compute_spearman
from corpus import normalize_corpora, create_vectors, relativization
from vectors import compare_vectors_distance, calculate_distance_between_vectors_in_interval, compare_sub_vectors_distance
from kilgarriff import compare_measurement, ksc_in_intervals, find_best_interval
from chi_square import create_contingency_table, chi_square
from euclidean import euclidean
from manhattan import manhattan
import csv


hp_corpus = read_txt('texts/HP.txt')
lotr_corpus = read_txt('texts/LOTR.txt')

normalized_hp_corpus, normalized_lotr_corpus = normalize_corpora(hp_corpus, lotr_corpus)

# best_spearman_interval = 10000 # find_best_interval(normalized_hp_corpus, normalized_lotr_corpus, compute_spearman)
# print('------')
# print(best_spearman_interval)
# print(compare_measurement(normalized_hp_corpus, normalized_lotr_corpus, compute_spearman))
# print('-----')
# print(ksc_in_intervals(normalized_hp_corpus, normalized_lotr_corpus, compute_spearman, best_spearman_interval, 10))

def compute_a_result(corpus1, corpus2, measurement):
    best_n = find_best_interval(corpus1, corpus2, measurement)
    result = ksc_in_intervals(corpus1, corpus2, measurement, best_n, 10)

    return result


csvfile = "./results/spearman.csv"
result = compute_a_result(normalized_hp_corpus, normalized_lotr_corpus, compute_spearman)

with open(csvfile, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(result)
