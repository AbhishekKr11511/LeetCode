'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# Solution
# Time complexity = O(2n) = O(n)
# -----------------------
from functools import reduce

def productExceptSelf(nums):
    answer = []
    # Got the product of the entire list
    productMaximus = reduce(lambda x,y : x*y,nums)

    for i,n in enumerate(nums):
        if n==0:
            exception = 1
            j = 0
            while j < len(nums):
                if j == i:
                    j+=1
                    continue
                exception = exception*nums[j]
                j += 1
            answer.append(exception)
            continue
        answer.append(productMaximus//n)
    return answer


print(productExceptSelf([-1,1,0,-3,3]))

