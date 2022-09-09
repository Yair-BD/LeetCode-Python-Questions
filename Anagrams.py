list = ["eat", "tea", "tan", "ate", "nat", "bat"]

def anagrams(list):
    final = []
    temp = {}
    for word in list:
        key_word = "".join(sorted(word))
        if key_word in temp:
            temp[key_word].append(word)
        else:
            temp[key_word] = [word]
    final.clear

    for b in temp.values():
        final.append(b)

    return final

print(anagrams(list))
