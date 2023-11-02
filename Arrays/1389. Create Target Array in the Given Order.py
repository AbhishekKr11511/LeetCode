def createTargetArray(nums, index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target

print(createTargetArray([1,2,3,4,0], [0,1,2,3,0]))