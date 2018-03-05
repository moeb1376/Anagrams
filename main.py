# -*- coding: utf-8 -*-
def set_words():
    words = set()
    with open('words.txt', 'r') as f:
        for line in f:
            words.add(line.strip())
    return words


def get_yechizi(word):
    result = []
    if len(word) == 1:
        return word
    for i in range(len(word)):
        temp = get_yechizi(word[:i] + word[i + 1:])
        result.extend([word[i] + j for j in temp])
    return result
words = set_words()
print(words.intersection(set(get_yechizi('مرگ'))))