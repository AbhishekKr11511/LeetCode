'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

# Brute Force method
# Time complexity = O(n*log(n) + n + k) => O(n*log(n))
#--------------------------
def topKFrequent(nums, k):
    myMap = {}
    for n in nums:
        if n not in myMap:
            myMap[n] = 0
        myMap[n] += 1
    sorted_map = dict(sorted(myMap.items(), key = lambda item : item[1]))
    filered_values = list(sorted_map.keys())
    print(filered_values)
    result = []
    for i in range(k):
        result.append(filered_values.pop())
    return result


# Optimized Force method
# This is time complexity O(n+n+n) => O(n)
#--------------------------
def topKFrequent2(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for n,c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res


print(topKFrequent2([4,1,-1,2,-1,2,3], 2))