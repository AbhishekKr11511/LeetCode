# from functools import reduce

nums = [10,4,8,3]
print(nums.index(10))
# maximus = max(nums)

# leftSum = reduce(lambda a, b: a+b, nums)

# print(maximus)
# print(leftSum)

# This is how to take inputs separated by a single space and form it into an array
# arr = list(map(int, input().split()))

# arr = [ 5,2,6,8,1,3]
# arr.sort(reverse=True)
# maximus = max(arr)
# for i in arr:
#     if i<maximus:
#         print(i, end=" ")
#         break

# arr = []
# scores = []
# names = []
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     minArr = [name, score]
#     arr.append(minArr)
#     scores.append(score)
# scores.sort()
# secminimum = scores[0]

# for i in range(len(scores)):
#     if(scores[i]>secminimum):
#         secminimum = scores[i]
#         break

# for j in range(len(arr)):
#     if(arr[j][1]==secminimum):
#         names.append(arr[j][0])
# names.sort()
# for k in range(len(names)):
#     print(names[k])

arr = list(map(str, input()))
newArr = list(map(lambda x:x.swapcase(), arr))
print("".join(newArr))


my_dict = {'A': 10, 'B': 5, 'C': 8, 'D': 12, 'E': 7}

max_pair = max(my_dict.items(), key=lambda x: x[1])

max_key, max_value = max_pair

print(f"The key with the maximum value is '{max_key}' with a value of {max_value}.")
