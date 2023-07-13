import collections


def group_anagrams(strs: list[str]) -> list[list[str]]:
    my_map = collections.defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        key = tuple(counts)
        my_map[key].append(s)
    return my_map.values()


if __name__ == "__main__":
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = [""]
    strs3 = [""]

    res1 = [["bat"], ["nat", "tan"], ["ate" , "eat", "tea"]]
    res2 = [[""]]
    res3 = [["a"]]

    all_strs = [strs1, strs2, strs3]
    for ss in all_strs:
        print(f"strs: {ss},\tgroup_anagrams(strs): {group_anagrams(ss)}\n")
