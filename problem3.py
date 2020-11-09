#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
import math

x= input("Enter a number:")
y= input("Enter a number:")
z= input("Enter a number:")
x= int(x)
y= int(y)
z= int(z)


if x < y and z < y:
    answer= pow(x,2)+pow(z,2)
    answer2= math.sqrt(answer)
    if answer2==y:
        x= str(x)
        y= str(y)
        z= str(z)
        print(x + "," + y + "," + z + ' ' + "form a Pythagorean triple")
    else:
        x= str(x)
        y= str(y)
        z= str(z)
        print(x + "," + y + "," + z + ' ' +  "do not form a Pythagorean triple")        

if y < z and x < z:
    answer= pow(y,2)+pow(x,2)
    answer2= math.sqrt(answer)
    if answer2==z:
        x= str(x)
        y= str(y)
        z= str(z)
        print(y + "," + x + "," + z + ' ' + "form a Pythagorean triple")
    else:
        x= str(x)
        y= str(y)
        z= str(z)
        print(y + "," + x + "," + z + ' ' +  "do not form a Pythagorean triple")


if z < x and y < x:
    answer= pow(z,2)+pow(y,2)
    answer2= math.sqrt(answer)
    if answer2==x:
        x= str(x)
        y= str(y)
        z= str(z)
        print(z + "," + y + "," + x + ' ' + "form a Pythagorean triple")
    else:
        x= str(x)
        y= str(y)
        z= str(z)
        print(z + "," + y + "," + x + ' ' +  "do not form a Pythagorean triple")







