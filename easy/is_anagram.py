"""
Implementation for leetcode problem to identify if two strings are anagrams.
"""

def is_anagram(s: str, t: str) -> bool:
    my_map = dict()
    for c in s:
        my_map.update({c: my_map.get(c, 0) + 1})
    for c in t:
        if c not in my_map:
            return False
        elif my_map.get(c) > 1:
            my_map.update({c: my_map.get(c) - 1})
        else:
            my_map.pop(c)
    return len(my_map) == 0


if __name__ == "__main__":
    s1 = "anagram"
    t1 = "nagaram"
    
    s2 = "rat"
    t2 = "car"

    string_list = [s1, t1, s2, t2]
    print(f"string_list: {string_list}")
    for str1 in string_list:
        for str2 in string_list:
            print(f"str1: {str1},\tstr2: {str2},\tis_anagram(str1, str2): {is_anagram(str1, str2)}\n")
            
