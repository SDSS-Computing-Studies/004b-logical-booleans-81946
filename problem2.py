#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
num= input("Enter a number")
num= int(num)

num2= input("Enter another number")
num2= int(num2)



if num > num2:
    if num % num2==0:
        num= str(num)
        num2= str(num2)
        print(num2 + ' ' + "is a factor of" + ' ' + num)
    else:
        num= str(num)
        num2= str(num2)
        print(num2 + ' ' + "is not a factor of" + ' ' + num)

num= int(num)
num2= int(num2)

if num2 > num:
    if num2 % num==0:
        num= str(num)
        num2= str(num2)
        print(num + ' '+ "is a factor of" + ' '+ num2)
    else:
        num= str(num)
        num2= str(num2)
        print(num + ' ' + "is not a factor of" + ' ' + num2)







