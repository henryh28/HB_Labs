"""Count words in file."""

import sys
word_count = {}

try:
    input_file = open(sys.argv[1])
except IndexError:
    print ("Please provide a file to process")
    exit()
except FileNotFoundError:
    print ("invalid filename")
    exit()

for line in input_file:
    line = line.split(" ")
    for word in line:
        if "\n" in word:
            word = word[:-2]
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

for key, value in word_count.items():
    print (key, value)

