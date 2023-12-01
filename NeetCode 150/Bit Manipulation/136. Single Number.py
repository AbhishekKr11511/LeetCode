'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''
# Time complexity = O(n)
# Space complexity = O(n)
def singleNumber(nums):
    mySet = set()
    for n in nums:
        if n not in mySet:
            mySet.add(n)
        else:
            mySet.remove(n)
    return list(mySet)[0]


# Time complexity = O(n)
# Space complexity = O(1)
def singleNumber2(nums):
    answer = 0
    for n in nums:
        answer = answer ^ n
    return answer

print(singleNumber2([4,1,2,1,2]))