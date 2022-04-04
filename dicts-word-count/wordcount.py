"""Count words in file."""

import sys

def main():
    words = read_input()
    print_output(words)

def read_input():
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
            word = word.strip('.,?";!_()').lower()
            word_count[word] = word_count.get(word, 0) + 1

    return (word_count)

def print_output(word_count):
    for key, value in word_count.items():
        print (key, value)

main()
