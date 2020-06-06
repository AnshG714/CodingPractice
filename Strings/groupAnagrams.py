from collections import defaultdict


def group(strs):
    """
    Given an array of strings, group anagrams together.

    Example:

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    """
    mapping = defaultdict(list)

    for string in strs:
        mapping[tuple(sorted([c for c in string]))].append(string)

    res = []
    for key in mapping.keys():
        res.append(mapping[key])

    return res
