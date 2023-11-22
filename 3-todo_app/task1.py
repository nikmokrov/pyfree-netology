#!/usr/bin/python3

def count_letter(words, letter):
    count = 0
    for word in words:
        if letter in word:
            count = count + 1
    return count

data = ['python', 'c++', 'c', 'scala', 'java']
print(count_letter(data, 'c'))
