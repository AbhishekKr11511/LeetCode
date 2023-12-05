'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
def search(nums, target):
    start = 0
    end = len(nums)
    mid = (start + end) // 2
    if end-start <= 1 and nums[mid] != target:
        return -1
    while target >= nums[start] and nums[end-1] >= target:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid+1
            mid = (start + end)//2
            continue
        elif nums[mid] > target:
            end = mid
            mid = (start+end)//2
    return -1

def search2(nums, target):
    if target < nums[0] or target > nums[-1]:
        return -1
    mid = len(nums) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return search2(nums[:mid], target)
    else:
        return search2(nums[mid:], target)

print(search2([-1,0,3,5,9,12],3))