'''
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# Solution
# Time complexity = O(n)

from collections import deque

def lengthOfLongestSubstring(s):
    myQueue = deque()
    maxlength = 0
    templength = 0
    for i,n in enumerate(s):
        if n not in myQueue:
            myQueue.append(n)
            templength += 1
            maxlength = max(maxlength, templength)
        else:
            j = 0
            while myQueue[j] != n:
                myQueue.popleft()
                templength -= 1
            myQueue.popleft()
            templength -= 1
            myQueue.append(n)
            templength += 1
    return maxlength


print(lengthOfLongestSubstring("bbbbb"))