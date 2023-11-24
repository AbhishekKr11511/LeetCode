arr1 = [1,1,1,2,2,2,3,3,3,4,4,5,5,5,6]

# Actuall approach
def removeDulples(array):
    newSet = []
    for i in range(len(array)-1):

        # Compare the next element
        if array[i] != array[i+1]:
            newSet.append(array[i])
    newSet.append(array.pop())
    return newSet


# Really fast but don't do this in interview
def getSet(array):
    newSet = set()
    newSet.update(array)
    return newSet

print(removeDulples(arr1))