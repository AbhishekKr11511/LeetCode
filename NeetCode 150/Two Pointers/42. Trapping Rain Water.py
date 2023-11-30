def trap(height):
    if len(height) < 3:
        return 0
    i = 0
    j = i+1
    area = 0
    start = height[i]
    end = height[j]
    minusthis = 0
    dummy = 0
    while j < len(height):
        if height[i] > height[j]:
            start = height[i]
            end = height[j]
            k = j
            
            while k < len(height):
                if height[k] > start:
                    break
                if height[k] >= height[j]:
                    dummy = minusthis
                    j = k
                minusthis += height[k]
                k += 1
            if k == len(height):
                k -= 1
            if height[j] < height[k]:
                j = k
                dummy = minusthis
            end = height[j]
            area += ((j-i-1) * min(start, end) - dummy)

            minusthis = 0
            dummy = 0
            i = j
            j += 1
        else:
            i = j
            j += 1
    return area


def trap2(height):
    if len(height) < 3:
        return 0
    area = 0
    maxleft = 0
    maxright = 0
    rightarray = []
    j = len(height)-2
    while j > 0:
        rightarray.append(max(maxright, height[j+1]))
        maxright = max(maxright, height[j+1])
        j -= 1
    rightarray.reverse()
    
    i = 1
    while i < len(height)-1:
        maxleft = max(maxleft, height[i-1])
        toparea = min(maxleft, rightarray[i-1]) - height[i]
        if toparea < 0:
            toparea = 0
        i += 1
        area += toparea
    return area



print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
# [4,2,0,3,2,5]
# [0,1,0,2,1,0,1,3,2,1,2,1]