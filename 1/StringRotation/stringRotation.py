from typing import Callable

def stringRotation(s1 : str, s2 : str) -> bool:
    length = len(s1)
    if length != len(s2):
        return False
    
    new_string = s1 + s1
    return isSubstring(s2, new_string)


def isSubstring(sub : str, big : str) -> bool:
    return sub in big

def test(func_version : Callable = stringRotation ):
    cases = [("waterbottle", "waterbottle"), ("waterbottle","erbottlewat"), ("testing","estingt"), ("estingt","testing"), ("a","aa"), (" ","a"), ("aaaba","abaaa"), ("the quick brown fox", "jumps over the lazy")]
    
    for case in cases:
        print(f'{case} : {func_version(*case)}')

test()