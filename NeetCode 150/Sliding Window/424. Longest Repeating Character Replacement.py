'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''

def characterReplacement(s, k):
    countMap = {}
    i = 0
    j = 0
    maximumResult = 0
    maxFreq = 0
    while j < len(s):
        countMap[s[j]] = countMap.get(s[j], 0) + 1
        
        maxFreq = max(list(countMap.values()))
        if k >= j - i + 1 - maxFreq:
            maximumResult = j-i+1
            j += 1
        else:
            i += 1
            j += 1
            countMap[s[i-1]] = countMap.get(s[i-1], 0) - 1
    
    return maximumResult

print(characterReplacement("AABABBA", 1))