'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4
'''

def largestRectangleArea(heights):
    stack = []
    maxArea = 0
    for i,h in enumerate(heights):
        j = 0
        while stack and stack[-1][1] > h:
            topIdx , topHeight = stack.pop()
            maxArea = max(maxArea, topHeight * (i-topIdx+j), h*(i-topIdx))
            i = topIdx
            j+=1
        stack.append([i,h])
    
    finalIndex = len(heights)
    # while stack:
    #     maxArea = max(maxArea, stack[-1][1] * (finalIndex - stack[-1][0]))
    #     stack.pop()
    for i, h in enumerate(stack):
        maxArea = max(maxArea, h[1]*(len(heights)-h[0]))
    return maxArea

print(largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))