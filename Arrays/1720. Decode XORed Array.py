def decode(encoded, first):
    arr = [first]
    for i in range(len(encoded)):
        arr.append(arr[i]^encoded[i])
    return arr

print(decode([1,2,3],1))