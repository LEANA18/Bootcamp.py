"""
Write a Python program to print a box like pattern of asterics (*) as shown below with size according to the input from the user.
"""



n=int(input())
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
