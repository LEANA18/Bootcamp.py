"""
Write a python function to check whether two strings are anagrams or not.
"""


def anagramfn(s1,s2):
    
    if(sorted(s1)== sorted(s2)):
        print("Yes")
    else:
        print("No")
x = input()
y = input()
anagramfn(x,y)
