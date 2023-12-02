

def reverse(x):
    i = 0
    sum = 0
    isneg = False
    if x < 0: isneg=True
    x = abs(x)
    digitArray= []
    while x:
        digitArray.append(x % 10)
        x //= 10
        i += 1
    j = 0
    while i>0:
        sum += digitArray[j] * (10**(i-1))
        i -= 1
        j += 1
    if sum < -2**31 or sum > 2**31:
        return 0
    elif isneg:
        return -sum
    else:
        return sum

print(reverse(120))