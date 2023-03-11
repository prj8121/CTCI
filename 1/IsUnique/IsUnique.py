from typing import Callable


# O(n^2)
def isUnique(string : str) -> bool:
    seen = []
    for char in string:     # happens n times
        if char in seen:    # This takes time equivalent to the length of the seen list
            return False
        seen.append(char)
    return True


# This is O(n) time
# Using ord() as the hash function means there is no collision
def isUniqueWithHashMap(string : str) -> bool:
    hmap = {}
    for char in string:         # happens n times
        res = hmap.get(ord(char))    # constant time to run ord and to access so 0(1)
        if res:
            return False
        else:
            hmap[ord(char)] = char    # O(1) since hash happens in constant time and dict lookup is O(1)
    return True


# This prints with ugly alignment
def test(isUniqueVersion : Callable = isUnique ):
    cases = ["asdf", "aasdf", "asdfa", "aA", "the quick brown fox jumps over the lazy dog", ""]
    
    for case in cases:
        print(f'{case} does{"" if isUniqueVersion(case) else " not"} consist of all unique characters')

test(isUniqueVersion=isUniqueWithHashMap)