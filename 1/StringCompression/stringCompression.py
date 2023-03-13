from typing import Callable

def stringCompression(string : str) -> str:

    length = len(string)
    if length <= 2:     # can't compress string of length < 2
        return string

    index = 0
    #total = 0
    #num_segments = 0
    current_char = string[0]
    consecutive_count = 0
    result = [""] * length # So we can operate on the result in place (and then return a slice)
    result_index = 0
    while index < length:
        if string[index] != current_char:   # if segment ends

            if result_index + 2 > length:   # + 2 because if the len(result) == len(string) we can't compress
                print("loc 1")
                return string

            # handle results of this segment
            result[result_index] = current_char
            result[result_index + 1] = str(consecutive_count)
            result_index += 2
            #total += consecutive_count
            #num_segments += 1

            # prepare for next segment
            current_char = string[index]
            consecutive_count = 1
        else:
            consecutive_count += 1
        index += 1

        if index == length:     # This code section will not run again because the string is over
            if result_index + 2 > length:   # + 2 because if the len(result) == len(string) we can't compress
                return string

            # handle results of this segment
            result[result_index] = current_char
            result[result_index + 1] = str(consecutive_count)
            result_index += 2

    
    return "".join(result[:result_index]) # [:result_index]



def test(func_version : Callable = stringCompression ):
    cases = ["aabbccddd", "aaaaaaaaaaa", "aaa", "aa", "a", "", "aAaAAA", "AAAAaAA"]
    
    for case in cases:
        print(f'{case} : {func_version(case)}')

test()