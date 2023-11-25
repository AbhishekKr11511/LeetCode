'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

# Brute force method
#-------------------------
def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    print(nums)
    count = 1
    max = 1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==0:
            continue
        if nums[i]-nums[i-1]==1:
            count+=1
            if max<count:
                max = count
        else:
            count = 1
    return max

# Optimize method
# Time complexity = O(n)
#--------------------------
def longestConsecutive2(nums):
    if len(nums) == 0:
        return 0
    newSet = set()
    newSet.update(nums)
    max = 1
    for n in newSet:
        count = 1
        if n-1 in newSet:
            continue
        if n+1 in newSet:
            temp = n+1
            while temp in newSet:
                count += 1
                temp += 1
            if max < count :
                max = count
    return max

print(longestConsecutive2([-6,8,-5,7,-9,-1,-7,-6,-9,-7,5,7,-1,-8,-8,-2,0]))
# print(longestConsecutive2([0,1,-1]))