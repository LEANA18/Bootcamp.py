"""
Rahul wrote a program to divide two numbers in python. On trying different input combinations, his code produced an error when the second input was chosen as zero. 
Rewrite the code raising an exception 'Cannot divide by zero!' to help Rahul run the code under such input conditions.
"""

x = int(input())
y = int(input())

try:
    z = x/y
    print(z)
except ZeroDivisionError as e:
    print('Cannot divide by zero!')
