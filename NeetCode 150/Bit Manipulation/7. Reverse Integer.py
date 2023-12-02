print(2**31)

def reverse(x):
    i = 1
    sum = 0
    digitArray= []
    while x:
        digitArray.append(x % 10)
        x //= 10
    print(digitArray)

print(reverse(123))