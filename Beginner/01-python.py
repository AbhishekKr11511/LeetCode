# name =  input("Enter Your name : ");
# print('Your name is : '+name)

# age = int(input("Your Age : "))
# print('You are '+str(age)+' years old ')

# if(age>=18):
#     print('You can vote :)')
# else:
#     print("You can't vote sorry :(")


# print(type(name))
# print(type(age))

# --------------------------------------------

number = int(input("Enter the length of the string : "))

array = []

for i in range(number):
    someNumber = int(input("Enter number : "))
    if(someNumber<10):
        array.append(someNumber)
    else:
        print('number greater than 10')
        
print(array)

#----------------------------------------------

