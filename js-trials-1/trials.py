"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print (item)


def get_all_evens(nums):
    return [x for x in nums if x % 2 == 0]


def get_odd_indices(items):
    return [item for item in items if items.index(item) % 2 != 0]


def print_as_numbered_list(items):
    return ("\n".join([value for value in [f"{item[0]+1}. {item[1]}" for item in enumerate(items)]]))

def get_range(start, stop):
    return list(range(start, stop))

def censor_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    string = ""

    for letter in word:
        string += letter if letter.lower() not in vowels else "*"

    return string    


def snake_to_camel(string):
    return "".join(word.capitalize() for word in string.split('_'))

def longest_word_length(words):
    return len(max(words, key=len))


def truncate(string):
    answer = string[0]
    
    for i in range(1, len(string)):
        if string[i] != answer[-1]:
            answer += string[i]
    
    return answer

def has_balanced_parens(string):
    stack = 0
    
    for char in string:
        if char == "(":
            stack += 1
        elif char == ")":
            stack -= 1
            
    return stack == 0

def compress(string):
  answer = ""
  counter = 1

  for i in range(len(string)-1):
    if string[i] != string[i+1]:
      if counter == 1:
        answer += string[i]
      else:
        answer += f"{string[i]}{counter}"
        counter = 1
    else:
      counter += 1

  if counter > 1:
    answer += f"{string[i]}{counter}"
  else:
    answer += string[-1]
   
  return answer

