from typing import Callable

def oneAway(s1 : str, s2 : str) -> bool:
    if len(s1) > len(s2):
        longer = s1
        shorter = s2
    else:
        longer = s2
        shorter = s1
    
    len_difference = len(longer) - len(shorter)

    if len_difference > 1:
        return False

    offset = 0
    index = 0
    while index < len(shorter):
        c1 = shorter[index]
        # Only read with offset if the strings aren't the same length
        c2 = longer[index] if len_difference == 0 else longer[index + offset]
        if c1 != c2:
            offset += 1
            if offset >= 2:     # offset convieniently also tracks the number of differences
                return False
            pass
            
        index += 1
    return True
    
# This prints with ugly alignment
def test(func_version : Callable = oneAway ):
    cases = [("abc","abcd"), ("abc", "abdc"), ("dabc", "abc"), ("adbc", "abc"), ("aaba", "aaab"), 
             ("spinning", "spining"), ("spinning", "pinning"), ("spinning", "pining"),
             ("pale", "ple"), ("pales", "pale"), ("pale", "bale"), ("pale", "bake"), 
             ("", "z"), ("",""), ("z", "a"), ("z", "z")]
    
    for case in cases:
        print(f'{case[0]}, {case[1]} : {func_version(*case)}')

test()