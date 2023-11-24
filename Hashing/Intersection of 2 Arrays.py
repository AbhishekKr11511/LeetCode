# Find the Intersection of these 2 arrays

arr1 = [1,5,5,8,1,8,7]
arr2 = [5,8,5,7,8,10]

# Naive approach
#--------------------------
def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)
    intersected = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                intersected.append(arr1[i])
                break
    print(intersected)


# Optimized method 1
# This method does include the repetetive elements, just the singular elements which are common
#--------------------------
def intersection2(arr1, arr2):
    hashSet1 = set()
    hashSet2 = set()
    hashSet1.update(arr1)
    hashSet2.update(arr2)
    intersectedSet = set()
    for n in hashSet1:
        if n in hashSet2:
            intersectedSet.add(n)
    return intersectedSet



# Optimized method 2
# This method does include the repetetive elements, just the singular elements which are common
#--------------------------
def intersection3(arr1, arr2):
    hashSet1 = set()
    hashSet2 = set()
    hashSet1.update(arr1)
    hashSet2.update(arr2)
    # Just use the inbuilt intersect method
    return hashSet2.intersection(hashSet1)

# intersection(arr1, arr2)

print(intersection2(arr1,arr2))
print(intersection3(arr1,arr2))