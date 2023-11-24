# Return the Union of 2 arrays
# Ignore the repetetive elements

arr1 = [5,8,5,7,8,10,15]
arr2 = [1,5,5,8,1,8,7,13]

# Normal approach
def unionFunc(arr1, arr2):
    myUnion = []

    for i in range(len(arr1)):
        if arr1[i] not in myUnion:
            myUnion.append(arr1[i])
            i += 1
    
    for j in range(len(arr2)):
        if arr2[j] not in myUnion:
            myUnion.append(arr2[j])
            j += 1
    return myUnion

#-------------------------------------

# Optimize (Cheating) approach
def getUnion(arr1, arr2):
    set1 = set()
    set2 = set()
    set1.update(arr1)
    set2.update(arr2)

    return set1.union(set2)

print(unionFunc(arr1,arr2))
print(getUnion(arr1,arr2))