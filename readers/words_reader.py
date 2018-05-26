import csv

def read_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        csv_file = csv.reader(file)
        corpus = [word[0] for word in csv_file]
    return corpus
