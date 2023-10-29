def shuffle(nums, n):
    output = []
    for i in range(n):
        output.append(nums[i])
        output.append(nums[n+i])
    return output