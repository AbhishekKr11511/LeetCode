# Merge 2 arrays in a sorted way 
# No don't return a union of the elements, return the merged so that duplicate elements are preserved


arr1 = [1,5,5,8,1,8,7,12]
arr2 = [5,8,5,7,8,10,13,14]

def merge(arr1, arr2):
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)
    mergedList = []
    i = 0
    j = 0
    while i < len(arr1):
        while j < len(arr2):
            if arr1[i]<=arr2[j]:
                mergedList.append(arr1[i])
                i += 1
                break
            else:
                mergedList.append(arr2[j])
                j += 1

    while j < len(arr2):
        mergedList.append(arr2[j])
        j += 1
    while i < len(arr1):
        mergedList.append(arr1[i])
        i += 1

    return mergedList

print(merge(arr1,arr2))