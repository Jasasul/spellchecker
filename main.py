from collections import OrderedDict

def remove_repeating(word):
    # shortens any characters that repeats more than 2 times in row to 2 of them
    res = ''
    for char in word:
        if len(res) < 2:
            res += char
        else:
            if char == res[-1] and char != res[-2] or char != res[-1]:
                res += char
    return res

def add_results(action_list, result_list):
    # adds results from the first list to the second list
    for result in action_list:
        if result not in result_list:
            result_list.append(result)

def addition(word, alphabet):
    # adds any letter from the alphabet anywhere in the word
    # and returns a list of those words
    results = []
    for i in range(len(word)):
        for j in range(len(alphabet)):
            added = word[:i] + alphabet[j] + word[i:]
            results.append(added)
    return results

def removal(word):
    # removes any letter from the word
    # and returns a list of those words
    results = []
    for i in range(len(word)):
        chars = list(word)
        chars[i] = ''
        results.append(''.join(chars))
    return results

def substitution(word, alphabet):
    # replaces a letter anywhere in the word with any letter from the alphabet
    # and returns a list of those words
    results = []
    for i in range(len(word)):
        for j in range(len(alphabet)):
            chars = list(word)
            chars[i] = alphabet[j]
            results.append(''.join(chars))
    
    return results

def transposition(word):
    # switch any 2 letters in a word
    # and returns a list of those words
    results = []
    for i in range(len(word)):
        for j in range(len(word)):
            chars = list(word)
            chars[i], chars[j] = chars[j], chars[i]
            transposed = ''.join(chars)
            if transposed not in results and transposed != word:
                results.append(transposed)

    return results



def edit(word):
    # 1 edit distance - additon, removal, substitution, transposition
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = []

    #adding results from those 4 actions
    add_results(addition(word, alphabet), results)
    add_results(removal(word), results)
    add_results(substitution(word, alphabet), results)
    add_results(transposition(word), results)
    
    return results

def more_edit(words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = []
    # if not found in first edit, continue
    for word in words:
        add_results(addition(word, alphabet), results)
        add_results(removal(word), results)
        add_results(substitution(word, alphabet), results)
        add_results(transposition(word), results)
    
    return results

def load_dict(file):
    dictionary = []
    with open(file, 'r', encoding='utf8') as f:
        for line in f.readlines():
            x = line.strip().split()
            while x[0].isnumeric():
              x.pop(0)
            word = (x[0], x[1] + x[2] + x[3]) 
            dictionary.append(word) 
    
    return dictionary

def binary_search (arr, l, r, value): 
    # returns index of a searched value in a dict
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid][0] == value: 
            return mid
        elif arr[mid][0] > value: 
            return binary_search(arr, l, mid-1, value) 
        else: 
            return binary_search(arr, mid + 1, r, value) 

    else: 
        return None

def in_dict(dictionary, word):
    # return True if word found
    x = binary_search(sorted_dict, 0, len(dictionary) - 1, word)
    if x != None:
        return True
    return False

dictionary = load_dict('word_dict.tsv')
sorted_dict = sorted(dictionary, key=lambda x: x[0])