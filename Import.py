"""
Zyphernova is a major country in a far away planet called Zentux. 
The Govt of Zyphernova is currently facing a economical crisis due to an ongoing war with the Planet Deltonia. 
Because of that, they are currenty charging very high Import duty on goods that are made in Deltonia, so that no body buys them!

The import duty is the factorial of cost of the goods! Which is super high!!.

Write a program that imports math module and uses its builtin fuctions to calculate the result.

The input will be a string of costs seperated with whitespace The output should be a string of total cost after adding import duty seperated in next lines
"""

import math
list=[]
list=[int(i) for i in input().split()]
leng=len(list)
for i in range(leng):
    list[i]=int(list[i])
for i in list:
    x=math.factorial(i)
    sum=i+x
    print(sum)
