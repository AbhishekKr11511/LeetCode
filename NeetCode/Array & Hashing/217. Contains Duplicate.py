'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# Solution 1
#----------------------

def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            return True
    return False


# Solution 2
#----------------------

def containsDuplicate2(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False




print(containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))