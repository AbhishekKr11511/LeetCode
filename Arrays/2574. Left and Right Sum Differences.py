from functools import reduce


def leftRightDifference(nums):
    answer = []
    for i in range(len(nums)):
        leftSum = sum(nums[0:i])
        rightSum = sum(nums[i+1:len(nums)])
        answer.append(abs(leftSum-rightSum))
    return answer

print(leftRightDifference([10,4,8,3]))