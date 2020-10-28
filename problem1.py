"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue.
"""

#! python3

q= input("Enter a number")
y= 0
q= float(q)

if q % 6==0 and q % 8 !=0:
    q= str(q)
    print(q +' ' + "is frue")
 
else:
    q= str(q)
    print(q + ' '+ "is not frue")

