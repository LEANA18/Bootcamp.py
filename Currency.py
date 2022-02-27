"""
Anson has a huge collection of currencies of different country. 
He decided to count the total number of distinct currencies in his collection. 
He asked for your help. 
You pick the currency notes one by one from a stack of N currency notes.

Find the total number of distinct currency notes.
"""

lst = []
n = int(input())
for i in range(0,n):
    item = input()
    lst.append(item)
lst_set = set(lst)
print(len(lst_set))
