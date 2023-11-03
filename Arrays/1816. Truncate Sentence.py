def truncateSentence(s, k):
    output = []
    input = s.split()
    for i in range(k):
        output.append(input[i])
    return " ".join(output)

print(truncateSentence("Hello how are you Contestant", 4))