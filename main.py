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