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
    alphabet = 'abcčdďefghijklmnopqrřsštťuvwxyzž'
    results = []

    #adding results from those 4 actions
    add_results(addition(word, alphabet), results)
    add_results(removal(word), results)
    add_results(substitution(word, alphabet), results)
    add_results(transposition(word), results)
    
    return results

def more_edit(words):
    alphabet = 'abcčdďefghijklmnopqrřsštťuvwxyzž'
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
            word = (x[0], x[1]) 
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

def in_dictionary(dictionary, word):
    # return True if word found
    x = binary_search(sorted_dict, 0, len(dictionary) - 1, word)
    return x

def correct_1(dictionary, word):
    avalible = []
    index = in_dictionary(dictionary, word)
    if index != None:
        avalible.append(dictionary[index])
        return avalible
    else:
        edit_1 = edit(word)
        for option in edit_1:
            index = in_dictionary(dictionary, option)
            if index != None:
                avalible.append(dictionary[index])
        return avalible
        # else:
        #     edit_2 = more_edit(edit_1)
        #     for option in edit_2:
        #         index = in_dictionary(dictionary, option)
        #         if index != None:
        #             avalible.append(dictionary[index])
        #     return avalible

def correct_2(options, word):
    edit_2 = more_edit(options)
    for option in edit_2:
        pass

def most_frequent(options):
    # finds a word from options with the highest frequency
    best = options[0]
    for option in options:
        if int(option[1]) > int(best[1]):
            best = option
    return best

def same_length(options, word):
    # returns a list of word with the same length as input word
    possibilities = []
    for option in options:
        if len(option[0]) == len(word):
            possibilities.append(option)
    return possibilities

def evaluate(options, word):
    if options == []:
        return word
    reduced = []
    if len(reduced) == 0:
        return most_frequent(options)[0]
    return most_frequent(reduced)[0]

def remove_prefix(word, special_chars):
    # removes special characters at the start of the word
    for i in range(len(word)):
        if word[i] not in special_chars:
            break
    no_special = word[i:]
    prefix = word[:i]

    return prefix, no_special
    

def remove_suffix(word, special_chars):
    # removes special characters at the end of the word\
    has_suffix = False
    for char in special_chars:
        if char in word:
            has_suffix = True
            break
    if has_suffix:
        for i in range(len(word)):
            if word[i] in special_chars:
                break
        no_special = word[:i]
        suffix = word[i:]
        return suffix, no_special
    return '', word

def clean_word(word):
    # removes special characters at the start and then at the end of the word
    if len(word) == 0:
        return '', word, ''
    special_chars = '"[](){}.,:;'
    prefix, no_prefix = remove_prefix(word, special_chars)
    suffix, no_suffix = remove_suffix(no_prefix, special_chars)
    return prefix, no_suffix, suffix

def join_prefix_suffix(prefix, word, suffix):
    # joins the given prefix and suffix to the word
    with_prefix = prefix + word
    with_suffix = with_prefix + suffix
    return with_suffix


dictionary = load_dict('word_dict.tsv')
sorted_dict = sorted(dictionary, key=lambda x: x[0])
with open('enigma_errors.txt', 'r', encoding='utf8') as f:
    string = f.read()
    new_string = ''
    for word in string.split(' '):
        prefix, cleaned, suffix = clean_word(word)
        x = evaluate(correct_1(sorted_dict, cleaned),cleaned)
        new_word = join_prefix_suffix(prefix, x, suffix)
        new_string += f'{new_word} '
with open('corrected.txt', 'w', encoding='utf8') as f:
    f.write(new_string)

