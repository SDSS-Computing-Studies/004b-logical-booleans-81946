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

lists= []

lists.append(x)
lists.append(y)
lists.append(z)

lists.sort()

a= lists[0]
b= lists[1]
c= lists[2]

if b < a and c < a:
    answer= pow(b,2)+pow(c,2)
    answer2= math.sqrt(answer)
    if answer2==a:
        a= str(a)
        b= str(b)
        c= str(c)
        print(a + "," + b + "," + c + ' ' + "form a Pythagorean triple")
    else:
        a= str(a)
        b= str(b)
        c= str(c)
        print(a + "," + b + "," + c + ' ' +  "do not form a Pythagorean triple")        

if a < b and c < b:
    answer= pow(a,2)+pow(c,2)
    answer2= math.sqrt(answer)
    if answer2==b:
        a= str(a)
        b= str(b)
        c= str(c)
        print(a + "," + b + "," + c + ' ' + "form a Pythagorean triple")
    else:
        a= str(a)
        b= str(b)
        c= str(c)
        print(a + "," + b + "," + c + ' ' +  "do not form a Pythagorean triple")


if b < c and a < c:
    answer= pow(a,2)+pow(b,2)
    answer2= math.sqrt(answer)
    if answer2==c:
        a= str(a)
        b= str(b)
        c= str(c)
        print(a + "," + b + "," + c + ' ' + "form a Pythagorean triple")
    else:
        a= str(a)
        b= str(b)
        c= str(c)
        print(a + "," + b + "," + c + ' ' +  "do not form a Pythagorean triple")







