from typing import Callable

def checkPermutation(s1 : str, s2 : str) -> bool:
    s1Chars = list(s1)
    s2Chars = list(s2)
    for char in s1Chars:
        try:
            s2Chars.remove(char)
        except ValueError:
            return False
    return len(s2Chars) == 0


def checkPermutationBySorting(s1 : str, s2 : str) -> bool:
    s1Chars = list(s1)
    s2Chars = list(s2)
    s1Chars.sort()
    s2Chars.sort()
    return s1Chars == s2Chars


def checkPermutationByFrequency(s1 : str, s2: str) -> bool:
    frequency = {}
    for char in s1:
        res = frequency.get(ord(char))
        if res:
            frequency[ord(char)] = res + 1
        else:
            frequency[ord(char)] = 1
    
    for char in s2:
        res = frequency.get(ord(char))
        if res:
            frequency[ord(char)] = res - 1
        else:
            return False
        
    return not any(frequency.values())

# This prints with ugly alignment
def test(checkPermutationVersion : Callable = checkPermutation ):
    cases = [("abc","cba"), ("aaaba", "abaaa"), ("aab", "abc"), ("abc", "aab"), ("abc", "abca"), ("abc", "abcdef")]
    
    for case in cases:
        print(f'{case[1]} is{"" if checkPermutationVersion(*case) else " not"} a permutation of {case[0]}')

test(checkPermutationVersion=checkPermutationByFrequency)