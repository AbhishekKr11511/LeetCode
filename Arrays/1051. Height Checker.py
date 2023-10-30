def heightChecker(heights):
    count = 0
    regular = heights[:]
    heights.sort()
    for i in range(len(heights)):
        if(heights[i]!=regular[i]):
            count +=1
    
    return count

heightChecker([10,6,6,10,10,9,8,8,3,3,8,2,1,5,1,9,5,2,7,4,7,7])