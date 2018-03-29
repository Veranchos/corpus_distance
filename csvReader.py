import csv


def read_csv(path):
    with open(path) as file:
        csv_file = csv.reader(file)
        corpus = [[key, int(value)] for key, value in csv_file]
    return corpus
