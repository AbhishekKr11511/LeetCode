'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''
def countOnes(num):
    count = 0
    while num > 0:
        count += num % 2
        num = num // 2
    return count

def countBits(n):
    output = []
    for i in range(n+1):
        output.append(countOnes(i))
    return output

print(countBits(5))