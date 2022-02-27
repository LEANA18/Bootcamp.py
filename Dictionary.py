"""
Given 5 pairs of numbers and names. 
You have to print out the names in ascending order based on the numbers assosciated with the name.
(Use python dictionary for this question)
"""

a={}
for i in range(5):
    data=input()
    k=data.split(' ')
    a[int(k[0])]=k[1]
d=sorted(a)
for i in range(5):
    print(a[d[i]])
