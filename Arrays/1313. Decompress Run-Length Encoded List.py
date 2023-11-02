def decompressRLElist(nums):
    output = []
    for i in range(0, len(nums),2):
        for j in range(0, nums[i]):
            output.append(nums[i+1])
    return output

print(decompressRLElist([1,2,3,4]))