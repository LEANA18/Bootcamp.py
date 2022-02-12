"""
Write a python program to print all the numbers in a given range that are divisible by 5 and numbers that are divisible by 3 but not divisible by both, 5 and 3.
"""

x = int(input())
y = int(input())
i=x
while i<=y:
    if i%5==0 and i%3==0:
        i=i+1
        continue;
    else:
        if i%5==0 or i%3==0:
            print(i)
    i=i+1
