def runningSum(nums):
    newArr = []
    for i in range(len(nums)):
        sum = 0
        for j in range(i+1):
            sum = sum + nums[j]
        
        newArr.append(sum)
    
    return newArr

print(runningSum([1,2,3,4]))