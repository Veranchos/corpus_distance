import csv

def read_csv(path):
    with open(path, 'r', encoding='utf-8') as file:
        csv_file = csv.reader(file)
        corpus = [[key.replace('\ufeff', ''), int(value)] for key, value in csv_file]
    return corpus
