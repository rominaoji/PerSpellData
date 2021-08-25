import numpy as np
import pandas as pd
import csv

xls = pd.ExcelFile('requierd_data/weights.xlsx')
df1 = pd.read_excel(xls, 'Transposition')
df2 = pd.read_excel(xls, 'Addition')
df3 = pd.read_excel(xls, 'Deletion')
df4 = pd.read_excel(xls, 'Substitution')
df1.rename({'Unnamed: 0': 'character'}, axis=1, inplace=True)
df2.rename({'Unnamed: 0': 'character'}, axis=1, inplace=True)
df4.rename({'Unnamed: 0': 'character'}, axis=1, inplace=True)
df1 = df1.set_index("character")
df2 = df2.set_index("character")
df4 = df4.set_index("character")

words = []
with open('requierd_data/1-gram.txt', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file]
for line in lines:
    words.append(line.split('\t')[0].strip())

allWords = []
max = 0
for word in words:
    if len(word) > max:
        max = len(word)

list_variable_length = []
list_fix_length = []
for length in range(2, max):
    if len(list_fix_length) != 0:
        list_variable_length.append(list_fix_length)
        list_fix_length = []
    for word in words:
        if len(word) == length:
            list_fix_length.append(word)


def edit_distance(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1

    tbl = {}
    for i in range(m): tbl[i, 0] = i
    for j in range(n): tbl[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            tbl[i, j] = min(tbl[i, j - 1] + 1, tbl[i - 1, j] + 1, tbl[i - 1, j - 1] + cost)

    return tbl[i, j]


with open('results/confusion_deletion.csv', 'a', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["word1", "word2", "type", "edit_distance", "no"])
    for word_length in range(0, max + 1):
        print("Deletion", word_length)
        if word_length != 0:
            for word1 in list_variable_length[word_length]:
                for word2 in list_variable_length[word_length - 1]:
                    if (edit_distance(word1, word2) == 1):
                        join_word = zip(word1, word2)
                        for char_word1, char_word2 in join_word:
                            if char_word1 != char_word2:
                                break
                        if (char_word1 == "\u200c" or char_word2 == "\u200c"):
                            writer.writerow([word1, word2, 2.6, "Deletion"])
                        else:
                            writer.writerow([word1, word2, 0, "Deletion"])
