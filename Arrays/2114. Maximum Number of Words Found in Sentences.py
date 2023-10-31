def mostWordsFound(sentences):
    max = 0
    for i in range(len(sentences)):
        temp = sentences[i].split(' ') # temo is an array
        if len(temp)>max:
            max = len(temp)
    return max

print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))