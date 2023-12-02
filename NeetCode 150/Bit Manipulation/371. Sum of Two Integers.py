'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
'''
def getSum(a,b):
    carr = 0
    sum = 0
    i = 0
    print(bin(a))
    print(bin(b))
    while a or b:
        aMod = a % 2
        bMod = b % 2
        if aMod+bMod+carr >= 2:
            sum += (2**i)*(aMod^bMod^carr)
            i += 1
            carr = 1
        else:
            sum += (2**i)*(aMod^bMod^carr)
            i += 1
            carr = 0
        a = a//2
        b = b//2
    if carr==1 :
        sum += (2**i)
    return int(sum)

print(getSum(10, -10))