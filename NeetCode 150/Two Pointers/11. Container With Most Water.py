def maxArea(height):
    maximum = 0
    length = len(height)
    i = 0
    j = length-1
    while i < j:
        while j > i:
            if height[i] < height[j]:
                area = (j-i) * height[i]
                maximum = max(maximum, area)
                i += 1
            else:
                area = (j-i) * height[j]
                maximum = max(maximum, area)
                j -= 1
            
    return maximum

print(maxArea([1,8,6,2,5,4,8,3,7]))

# [1,8,6,2,5,4,8,3,7]