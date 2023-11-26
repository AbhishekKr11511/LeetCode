'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
# Brute Force method
#--------------------------
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                print([nums[i], nums[j]])
    return False


# Optimized method
#--------------------------
def twoSum2(nums, target):
    for i in range(len(nums)):
        newHashSet = set()
        newHashSet.update(nums[i+1: len(nums)])
        if (target-nums[i]) in newHashSet:
            return [i, (nums[i+1: len(nums)].index(target-nums[i]))+i+1]
    return False

# Optimized method 2
#--------------------------
def twoSum3(nums, target):
    hashMap = {}
    for i,n in enumerate(nums):
        diff = target-n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i



print(twoSum([-3, 8, 3, 7, 6, 2, 4, 1], 5))