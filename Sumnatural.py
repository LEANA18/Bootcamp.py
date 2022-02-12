"""
Write a python program to print the sum of first 'n' numbers using a 'for' loop
"""

n=int(input())
sum=0
for i in range(0,n+1):
    sum=sum+i
print("The sum is",sum)
