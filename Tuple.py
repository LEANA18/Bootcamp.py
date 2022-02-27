"""
Given an integer n and n space-separated integers as input, create a tuple, t , of those n integers. 
Then compute the product of all numbers in the given tuple
"""

n= int(input())
tuple = tuple(input().split(" "))
prod = 1
for i in tuple:
    prod=prod*(int(i))
    
print(prod)
