#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    r = list(a_dictionary.keys())[0]
    big = a_dictionary[r]
    for i, j in a_dictionary.items():
        if j > big:
            big = j
            r = i
    return (r)
