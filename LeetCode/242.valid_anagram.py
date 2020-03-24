def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    dict = {}
    for ch in str1:
        if ch not in dict:
            dict[ch] = 1
        else:
            dict[ch] += 1
    for ch in str2:
        if ch not in dict:
            return False
        else:
            dict[ch] -= 1
    return all(val == 0 for val in dict.values())


print(is_anagram("anagram", "anagram"))
