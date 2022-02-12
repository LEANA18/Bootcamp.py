"""
Write a Python program to print the required output based on the number of rows taken from user input
"""

n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='')
    print("")        
        
    
