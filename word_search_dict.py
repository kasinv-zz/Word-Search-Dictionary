
'''
function found_word
inputs: word => alphameric word
        dic => the dictionary of words

output: found => if lower-case of the word is found in the dic
        dic_word => tuple (frequency, matching string)
'''
def found_word(word, dic):
    '''
    checks to see if word is already in dictionary
    returns word and accompanying value
    '''

    dic_word = ()
    w = word.casefold()
    
    if w in dic:
        dic_word = (dic[w], word)

    return dic_word


  
'''
function drop_letter
drops a letter from the word and see if the new word has a match in dictionary
inputs: word => alphameric word
        dic => the dictionary set of words

output: dic_word => set of tuples (frequency, matching word)
'''
def drop_letter(word, dic):

    '''
    loop through the word, drop one letter to create a new word
    see if the new word is found in the dic
    if found, add it to the set found_words
    in the end, return set of matches and its frequencies
    '''

    found_words = set()
    
    for i in range(len(word)):
        new_word = word[:i] + word[(i+1):]
        dic_word = found_word(new_word, dic)
        if dic_word:
            found_words.add(dic_word)
        
    return found_words


'''
function insert_letter
insert a letter into the word from start, and see if the new word has a match in dictionary
inputs: word => alphameric word
        dic => the dictionary set of words

output: dic_word => set of tuples (frequency, matching word)
'''

def insert_letter(word, dic):

    '''
    loop through the word, add one letter at a time to create a new word
    see if the new word is found in the dic
    if found, add it to the set found_words
    in the end, return set of matches and its frequencies
    '''
    
    found_words = set()
    

    letters = [chr(x+97) for x in range(0,26)]

    for i in range(len(word)+1):
        for j in range(len(letters)):
            new_word = word[:i] + letters[j] + word[i:]
            dic_word = found_word(new_word, dic)
            if dic_word:
                found_words.add(dic_word)

    return found_words

'''
function swap_letter
swaps two consecutive letters in a word, and check if new word has a match in dictionary
inputs: word => alphameric word
        dic => the dictionary set of words

output: dic_word => set of tuples (frequency, matching word)
'''
def swap_letter(word, dic):
    '''
    loop through the word from start to the last-but-one letter
    pull out the ith letter and the (i+1) letter
    restring new word as follows
    see if the new word is found in the dic
    if found, add it to the set found_words
    in the end, return set of matches and its frequencies
    '''

    found_words = set()

    for i in range(len(word)-1):
        initial_letter = word[i]
        next_letter = word[i+1]

        new_word = word[:i] + next_letter + initial_letter + word[(i+2):]

        dic_word = found_word(new_word, dic)
        if dic_word:
            found_words.add(dic_word)

    return found_words


'''
function replace_letter
replace each letter with letters from the alphabet, and check if new word has a match in dictionary
inputs: word => alphameric word
        dic => the dictionary set of words
        keyboard_dic => dictionary of {letter, list of swappable keyboard letters}

output: dic_word => set of tuples (frequency, matching word)
'''
def replace_letter(word, dic, keyboard_dic):
    '''
    loop through the letters of the word
    inner loop through key_set values for the letter as a key
    restring a new word as follows
    see if the new word is found in the dictionary
    if found, add it to the set found_words
    in the end, return set of matches and its frequencies
    '''

    found_words = set()
    
    for i in range(len(word)):
        if word[i] in keyboard_dic:
            for letter in keyboard_dic[word[i]]:
                new_word = word[:i] + letter + word[i+1:]
                dic_word = found_word(new_word, dic)
                if dic_word:
                    found_words.add(dic_word)

    return found_words



dic_file = input("Dictionary file => ")
print(dic_file)
dic_set = dict(line.casefold().strip().split(',')
            for line in open(dic_file, 'r', encoding='utf-8'))

#read dictionary of all words into dictionary
dictionary_dic = dict()
for line in open(dic_file):
    line = line.strip()
    line = line.split(",")
    word = line[0]
    value = line[1]
    dictionary_dic[word] = value


# read the input words file into a list word_list, as-is
input_file = input("Input file => ")
print(input_file)
word_list = list(line.strip()
              for line in open(input_file, 'r', encoding='utf-8'))


# read keyboard letters into a set called key_set, in lowercase
keyboard_file = input("Keyboard file => ")
print(keyboard_file)
key_set = {str(line.casefold().strip().split(' ')[0]):
        list(line.casefold().strip().split(' ')[1:])
        for line in open(keyboard_file, 'r', encoding='utf-8')}


# for each word in the input file, check matches in dictionary and
# print result
for w in word_list:
    
    dic_word = found_word(w, dic_set)
    if dic_word:
        result = ":FOUND"
        print("{:15}".format(w), "->", "{:15}".format(dic_word[1]), result)
        
    else:
        dic_word = set()
        dic_word.update(drop_letter(w, dic_set))
        dic_word.update(insert_letter(w, dic_set))
        dic_word.update(swap_letter(w, dic_set))
        dic_word.update(replace_letter(w, dic_set, key_set))

        n = 3
        dic_word_n = sorted(dic_word, reverse=True)
        dic_word_n = dic_word_n[:n]
        result = ":MATCH"

        if dic_word_n:
            for i in range(len(dic_word_n)):
                print("{:15}".format(w), "->", "{:15}".format(dic_word_n[i][1]), result, i+1)

        else:
            result = ":NO MATCH"
            print("{:15}".format(w), "->", "{:15}".format(w), result)

if __name__ == "__main__":

    pass
