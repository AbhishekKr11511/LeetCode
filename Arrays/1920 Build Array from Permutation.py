def buildArray (nums):
    output = []
    length = len(nums)
    for i in range(length):
        output.append(nums[nums[i]]);
    return output

result = buildArray([0,2,1,5,3,4])

print(result)