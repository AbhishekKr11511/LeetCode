def smallerNumbersThanCurrent(nums):
    output = []
    for i in range(len(nums)):
        count = 0
        for j in range (len(nums)):
            if(nums[i]>nums[j]):
                count += 1;
        
        output.append(count)
    return output


print(smallerNumbersThanCurrent([8,1,2,2,3]))