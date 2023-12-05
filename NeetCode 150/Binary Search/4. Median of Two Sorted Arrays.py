'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
class TimeMap(object):

    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        if key in self.time_map:
            self.time_map.get(key)[timestamp] = value
            return
        self.time_map[key] = {timestamp: value}
        

    def get(self, key, timestamp):
        if key in self.time_map:
            self.keyMap = self.time_map[key]
            while timestamp > 0:
                if timestamp in self.keyMap:
                    return self.keyMap[timestamp]
                else:
                    timestamp -= 1
        return ""
    
    def display(self):
        print(self.time_map)


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
timeMap.set("foo", "bar2", 4)

timeMap.display()

# print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
# timeMap.get("foo", 3)
# timeMap.get("foo", 4)
# timeMap.get("foo", 5)
