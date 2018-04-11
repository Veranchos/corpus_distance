def read_txt(file_name):
    word_list = []
    with open(file_name) as file:
        for string in file:
            elem = string.split('\t')
            key, value = elem[2], float(elem[1])
            word_list.append([key.replace('\n', ''), value])
    return word_list