def numsum(num):
    sum = 0
    for d in num:
        sum = sum + int(d)
    return sum 

def differenceOfSum(nums):
    numsSum = sum(nums)
    
    digitsum = 0
    for i in range(len(nums)):
        digitsum = digitsum + numsum(str(nums[i]))
    return abs(numsSum-digitsum)

print(differenceOfSum([1,15,6,3]))
