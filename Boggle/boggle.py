"""
File: boggle.py
Name: Eva
----------------------------------------
"""

import time


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    start = time.time()

    # Check input validity
    legal = True
    d = {} # {(0,0): 'f', ...}
    lst = []
    for i in range(4):
        row = str(input(f'{i} row of letters: '))
        if len("".join(row.split())) != 4:
            legal = False
        for ch in "".join(row.split()):
            if not ch.isalpha():
                legal = False
        for j in range(1, len(row), 2):
            if row[j] != " ":
                legal = False
        if not legal:
            print('Illegal input')
            break

        for j in range(len(row.split())):
            d[(i, j)] = row.split()[j]

    # Search for words
    found_words = set()
    used = set()
    w_dict = read_dictionary()
    for i in range(4):
        for j in range(4):
            center = d[(i, j)]
            used.add((i, j))
            ans = center
            find_words(d, used, ans, found_words, i, j, w_dict)
            used.remove((i, j))

    # Print found words
    for word in found_words:
        print(f'Found "{word}"')

    # Print total count
    print(f"There are {len(found_words)} in total")

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(d, used, word, found_words, x, y, w_dict):
    if not has_prefix(word):
        return
    else:
        if len(word) >= 4:
            if word in w_dict and word not in found_words:
                found_words.add(word)
                print(f'found: {word}')
                print('Searching...')
        for i in range(-1,2):
            for j in range(-1,2):
                if (x+i, y+j) not in used and 0 <= x+i <4 and 0 <= y+j <4:
                    word += d[(x+i, y+j)]
                    used.add((x+i, y+j))
                    find_words(d, used, word, found_words, x+i, y+j, w_dict)
                    word = word[:-1]
                    used.remove((x+i, y+j))


def find_neighbors(row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            cur_row = (i - 1) % 4 + 1
            cur_col = (j - 1) % 4 + 1
            if cur_row == row and cur_col == col:
                continue
            neighbors.append((cur_row, cur_col))
    return neighbors


def get_key_by_tuple(d, tuple_value):
    for ch, tuples in d.items():
        for item in tuples:
            if item == tuple_value:
                return ch


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dic_lst = set()
    with open(FILE, 'r') as f:
        for line in f:
            token = line.strip()
            if len(token) >= 4:
                dic_lst.add(token)
    return dic_lst


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    dic_lst = read_dictionary()
    for voc in dic_lst:
        if voc.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
