# Resturn the distinct elements of the array

# Method 1
#---------------------------
def countDistinct(array):
    hashSet = set()
    for n in array:
        # hashing in default doesn't duplicate values
        hashSet.add(n)
    return hashSet

# Method 2 
#---------------------------
def countDistinct2(array):
    hashSet = set()
    hashSet.update(array)
    return hashSet


print(countDistinct2([1,2,3,4,1,2,3,8,9]))