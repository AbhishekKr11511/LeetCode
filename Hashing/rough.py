
# Time Complexity :O(n)
# Space Complexity : O(n)
def pairSum(arr, sum):

    set1 = set()

    for i in range(len(arr)):
        if sum - arr[i] in set1:
            print(arr[i], sum-arr[i])

        set1.add(arr[i])


# Driver Code
arr = [-3, 8, 3, 7, 6, 2, 4, 1]
sum = 5
pairSum(arr, sum)