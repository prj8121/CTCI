def URLify(string : str, space : int) -> str:
    str_arr = list(string)
    parse_index = space - 1         # Index to parse
    place_index = len(str_arr) - 1  # Index to place character in

    while parse_index > 0:
        if str_arr[parse_index] != " ":
            str_arr[place_index] = str_arr[parse_index]
            place_index -= 1
        else:
            # This slicing is weird and "risky" but since we are guarenteed to have enough space it should work
            str_arr[place_index-2:place_index+1] = "%20"
            place_index -= 3
        parse_index -= 1
    
    return "".join(str_arr)

print(URLify("Mr John Smith    ", 13))