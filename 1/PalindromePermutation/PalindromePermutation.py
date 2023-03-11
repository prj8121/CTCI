from typing import Callable

def palindromePermutation(string : str):
    string = string.replace(" ", "")    # O(n) removal of spaces
    string = string.lower()             # O(n) ignoring case
    frequency = {}

    for char in string:
        res = frequency.get(ord(char))
        if res:
            frequency[ord(char)] = res + 1
        else:
            frequency[ord(char)] = 1
    
    # The number of characters with odd frequency
    num_odd = sum([val % 2 for val in frequency.values()])

    if num_odd >= 2:
        return False

    # If even length -> num_odd must be 0, If odd length -> num_odd must be 1
    return len(string) % 2 == num_odd


def test(func_version : Callable = palindromePermutation ):
    cases = ["abc", "tacocat", "Tact coa", "p p p pa a v"]
    
    for case in cases:
        print(f'{case}:{func_version(case)}')

test()