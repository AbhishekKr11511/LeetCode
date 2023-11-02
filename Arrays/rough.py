from functools import reduce

nums = [10,4,8,3]
bro = []

leftSum = reduce(lambda a, b: a+b, nums)

print(leftSum)