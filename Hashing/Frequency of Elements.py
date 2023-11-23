# return a frequency of each elements in an array


# Method 1 (Print an dictionary)
#---------------------------------
def countFrequency(array):
    hashMap = dict()

    # Omit this line if no need for ordered dictionary
    array.sort()
    for i in range(len(array)):
        if array[i] in hashMap:
            hashMap[array[i]] += 1
        else:
            hashMap[array[i]] = 1
    for n in hashMap:
        print(f"{n} : {hashMap[n]}")


countFrequency([1,2,3,4,3,2,6,2,3,4,2,1,0,1])