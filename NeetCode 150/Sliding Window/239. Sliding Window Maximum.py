'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
def maxSlidingWindow(nums, k):
    i = 0
    j = k-1
    result = []
    maximum = 0
    while j<len(nums):
        if len(result) == 0:
            result.append(max(nums[i:j+1]))
            maximum = result[-1]
            i += 1
            j += 1
            continue
        if nums[i-1] != maximum:
            result.append(max(maximum, nums[j]))
            maximum = result[-1]
        else:
            
            result.append(max(nums[i:j+1]))
            maximum = result[-1]
        i += 1
        j += 1
    return result

from collections import deque

# Efficient Algorithm:
def maxSlidingWindow2(nums, k):
    output = []
    que = deque()
    i = j = 0
    
    while j < len(nums):
        # pop smaller values from q
        while que and nums[que[-1]] < nums[j]:
            que.pop()
        que.append(j)

        # remove left value from window
        if i > que[0]:
            que.popleft()
        
        if ( j + 1 ) >= k :
            output.append(nums[que[0]])
            i += 1
        
        j += 1
        
    return output

print(maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3))