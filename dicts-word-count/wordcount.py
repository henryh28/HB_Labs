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
    line = line.rsplit()
    for word in line:
        word_count[word] = word_count.get(word, 0) + 1

for key, value in word_count.items():
    print (key, value)

