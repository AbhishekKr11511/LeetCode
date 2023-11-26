'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

# strs being an array of strings


# Brute Force method 
# Time complexity O(m * n log(n))
# Where n is the average length of the string and m is the number of elements in the strs list.
#--------------------------
def sortify(n):
    return "".join(sorted(n))

def groupAnagrams(strs):
    hashMap = {}
    for n in strs:
        sortedString = sortify(n)
        
        if sortedString not in hashMap:
            hashMap[sortedString] = []
        
        hashMap[sortedString].append(n)
        
    return list(hashMap.values())

# Optimized Force method
#--------------------------
from collections import defaultdict


def groupAnagrams2(strs):
    res = defaultdict(list) # Mapping character count to list of Anagrams
    for s in strs:
        count = [0] * 26 # For all characters : a.....z
        
        for c in s:
            # ord() returns the ascii value of characters
            count[ord(c)-ord('a')] += 1
        
        res[tuple(count)].append(s)

    return list(res.values())




print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))