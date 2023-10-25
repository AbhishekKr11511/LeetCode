n = 10

arr = [1]*n

print(arr)

# a, b, c = [2, 4, 8]
# print(a,b,c)



# myArray = [1,2,3,4,5,6,7,8,9]

# for i in range(len(myArray)):
#     print(myArray[i], end=" ")

# print('\nSecond loops')

# myArray.reverse()

# for n in myArray:
#     print(n, end=" ")
    


# arr = [[i*j for i in range(4)] for j in range(4)]
# print(arr)

myString = 'abcdefg'
print(myString[:])

# Strings are immutable

print(str(100)+str(100))
print(int('100')+int('100'))

# For the ascii value for a character
print(ord('b'))
print(ord('@'))


#Functions

def myFunc(n,m):
    return n*m

print(myFunc(2,6))