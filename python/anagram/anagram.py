def detect_anagrams(word, choices):
    ret = []
    dic = {}
    if word == choices[0]:
        return ret
    word = word.lower()
    for char in word:
        dic[char] = dic.get(char, 0) + 1

    for choice in choices:
        dic2 = {}
        for char in choice:
            dic2[char.lower()] = dic2.get(char.lower(), 0) + 1
        if dic == dic2:
            ret.append(choice)

    return ret
