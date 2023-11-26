'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
# Brute force method, has time complexity of O(n^3)
def threeSum(nums):
    length = len(nums)
    array = {}
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if nums[i]+nums[j]+nums[k] == 0:
                    array.add(sorted([nums[i], nums[j], nums[k]]))
    return array

def threeSum2(nums):
    newSet = set()
    result = []
    newSet.update(nums)
    print("newSet : ", newSet)
    for n in newSet:
        find = -n
        subSet = set()
        subSet.update(newSet)
        subSet.remove(n)
        print("subSet : ", subSet)
        for m in subSet:
            diff = find - m
            if diff in subSet:
                result.append([n,m, diff])
    return result



print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,0,0]))
