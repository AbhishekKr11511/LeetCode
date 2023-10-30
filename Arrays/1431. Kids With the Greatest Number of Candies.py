def kidsWithCandies(candies,extraCandies):
    result = []
    maximum = max(candies)
    print(max)
    for n in candies:
        if(n+extraCandies >= maximum):
            result.append(True);
        else:
            result.append(False)
        
    return result

print(kidsWithCandies([2,3,5,1,3], 3))