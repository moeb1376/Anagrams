# -*- coding: utf-8 -*-
import time


def set_words():
    words = set()
    with open('words.txt', 'r') as f:
        for line in f:
            words.add(line.strip())
    return words


def get_permutation(word):
    result = []
    if len(word) == 1:
        return word
    for i in range(len(word)):
        temp = get_permutation(word[:i] + word[i + 1:])
        result.extend([word[i] + j for j in temp])
    return result


t = time.time()
words = set_words()
print(words.intersection(set(get_permutation('مرگ'))))
print(time.time() - t)
del words


def set_words2():
    words2 = {}
    with open('words.txt', 'r') as f:
        hamze = ord('ء')
        for line in f:
            word = line.strip()
            count = 0
            for c in word:
                count += (ord(c) - hamze)
            data = words2.get(count, [])
            if data != []:
                words2[count].append(word)
            else:
                words2[count] = [word]
    return words2

t = time.time()
words = set_words2()
hamze = ord('ء')
count = sum([ord(i)-hamze for i in 'مرگ'])
search_area = words[count]
per = get_permutation('مرگ')
for i in per:
    if i in search_area:
        print(i)
print(time.time() - t)