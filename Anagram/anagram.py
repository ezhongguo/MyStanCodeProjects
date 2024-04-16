"""
File: anagram.py
Name: Eva
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This function finds all the anagram(s) for the word input by user.
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        print('Searching...')
        if s == EXIT:
            break
        else:
            anagrams_lst = []  # List to store the found anagrams
            for permutations in find_anagrams(s):
                if permutations in read_dictionary():
                    if has_prefix(permutations):
                        print('Found: '+str(permutations))
                        print('Searching...')
                        anagrams_lst.append(permutations)
            print(str(len(anagrams_lst))+" anagrams: "+str(anagrams_lst))
    end = time.time()
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    voc_dic = []
    with open(FILE, 'r') as f:
        for line in f:
            tokens = line.split()
            for token in tokens:
                voc_dic.append(token)
    return voc_dic


def find_anagrams(s):
    """
    :param s: str, entered by the user
    :return: list, all permutations of s
    """
    permutations = []  # List to store all permutations
    find_anagrams_helper(s, "", [], [], permutations)
    return permutations


def find_anagrams_helper(s, current_s, pair_lst, index_lst, permutations):
    if len(current_s) == len(s) and current_s not in permutations:
        permutations.append(current_s)
    else:
        for i in range(len(s)):
            ch = s[i]
            index = i
            pair = (ch, index)
            if pair not in pair_lst:  # Check if the pair is already chosen
                pair_lst.append(pair)
                index_lst.append(index)
                # Choose
                current_s += ch
                # Explore
                find_anagrams_helper(s, current_s, pair_lst, index_lst, permutations)
                # Un-choose
                pair_lst.pop()
                index_lst.pop()
                current_s = current_s[:len(current_s) - 1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return: boolean
    """
    voc_lst = read_dictionary()
    for voc in voc_lst:
        if voc.startswith(sub_s):
            return True
    return False




if __name__ == '__main__':
    main()
