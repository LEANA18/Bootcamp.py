"""
Write a Python program to print the required output based on the number of rows taken from user input.
"""

n = int(input())
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")
