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
def findMedianSortedArrays(nums1, nums2):
    fullList = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i]<nums2[j]:
            fullList.append(nums1[i])
            i += 1
        else:
            fullList.append(nums2[j])
            j += 1
    while j < len(nums2):
        fullList.append(nums2[j])
        j += 1
    while i < len(nums1):
        fullList.append(nums1[i])
        i += 1
    print(fullList)
    fulllength = len(fullList)
    if fulllength%2 == 0:
        median = (fullList[fulllength//2 - 1] + fullList[fulllength//2])/2
        return median
    else:
        median = fullList[fulllength//2]
        return median


print(findMedianSortedArrays([1,2], [3,4]))
