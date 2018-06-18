from readers.words_reader import read_words
from spearman import compute_spearman
from corpus import normalize_corpora
from vectors import calculate_vectors_distance
from kilgarriff import create_wordlist, ksc_in_intervals
from chi_square import chi_square
from euclidean import euclidean
from manhattan import manhattan
import os
import csv

def compute_a_result(corpus1, corpus2, measurement):
    return ksc_in_intervals(corpus1, corpus2, measurement, 200, 5)

def compute_all_measurements_for_two_corpora(corpus1, corpus2, directory):
    csvfile = directory + "spearman.csv"
    result = compute_a_result(corpus1, corpus2, compute_spearman)

    with open(csvfile, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(result)

    csvfile1 = directory + "euclidean.csv"
    result1 = compute_a_result(corpus1, corpus2, euclidean)

    with open(csvfile1, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(result1)
    #
    csvfile2 = directory + "manhattan.csv"
    result2 = compute_a_result(corpus1, corpus2, manhattan)

    with open(csvfile2, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(result2)

    csvfile3 = directory + "cosine.csv"
    result3 = compute_a_result(corpus1, corpus2, calculate_vectors_distance)

    with open(csvfile3, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(result3)

    csvfile4 = directory + "chi_square.csv"
    result4 = compute_a_result(corpus1, corpus2, chi_square)

    with open(csvfile4, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(result4)

def compute_all_data():
    corpora_names = [name for name in map(lambda filename: os.path.splitext(filename)[0], os.listdir('./words/'))]

    for i1 in range(len(corpora_names)):
        for i2 in range(i1+1, len(corpora_names)):
            corpus_name1 = corpora_names[i1]
            corpus_name2 = corpora_names[i2]

            corpus1 = read_words(f'words/{corpus_name1}.csv')
            corpus2 = read_words(f'words/{corpus_name2}.csv')

            directory = f"./results/{corpus_name1}-{corpus_name2}/"

            if not os.path.exists(directory):
                os.makedirs(directory)

            compute_all_measurements_for_two_corpora(corpus1, corpus2, directory)

def save_corpora_wordlists():
    corpora_names = [filename for  filename in map(lambda filename: os.path.splitext(filename)[0], os.listdir('./words/'))]

    for i1 in range(len(corpora_names)):
        for i2 in range(i1, len(corpora_names)):
            if (i1 != i2):
                corpus_name1 = corpora_names[i1]
                corpus_name2 = corpora_names[i2]
                corpus1 = read_words(f'words/{corpus_name1}.csv')
                corpus2 = read_words(f'words/{corpus_name2}.csv')
                n_corpus1, n_corpus2 = normalize_corpora(create_wordlist(corpus1), create_wordlist(corpus2))

                with open(f'wordlists/{corpus_name1}-{corpus_name2}({corpus_name1}){len(n_corpus1)}.csv', "w", encoding='utf-8') as output:
                    writer = csv.writer(output, lineterminator='\n')
                    writer.writerows(n_corpus1)
                with open(f'wordlists/{corpus_name1}-{corpus_name2}({corpus_name2}){len(n_corpus1)}.csv', "w", encoding='utf-8') as output:
                    writer = csv.writer(output, lineterminator='\n')
                    writer.writerows(n_corpus2)
                print(corpus_name1, corpus_name2, len(n_corpus1))