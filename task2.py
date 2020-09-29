#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

q= input("Please enter a number: ")
a= float(q) 
b= math.sqrt(a)     
d= int(q)
c= math.sqrt(d)
c= int(c)

s= math.pow(a,(1.0/3))
z= math.pow(d,(1.0/3))
s= round(s,10)
z= round(z,10)
z=int(z)
if b==c and s==z:
    print(q+' '"is both a perfect square and a perfect cube")
    
    
elif b==c:
    print(q+' '"is only a perfect square")
    

elif s==z:
    print(q+' '"is only a perfect cube")

else:
    print(q+' '"Not a perfect cube or a perfect square")


