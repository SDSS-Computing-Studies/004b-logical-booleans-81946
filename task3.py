#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""

q= input("Please enter a number: ")
a= float(q)

if a > 0:
    print(q+' '"is a positive number")

elif a==0:
    print(q+' '"can't be negative or positive")

else:
    print(q+' '"is not a positive number")
    

