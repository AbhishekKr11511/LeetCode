def arrayStringsAreEqual(word1, word2):
    str1 = "".join(word1)
    str2 = "".join(word2)
    if str1==str2:
        return True
    else:
        return False

print(arrayStringsAreEqual(["ab", "c"],["a", "bc"]))