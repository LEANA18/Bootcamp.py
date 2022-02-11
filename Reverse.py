"""
Write a python program to accept two strings as input. Each line of the input will be a name in reverse. 
Print a wedding card that displays “ Name-1 weds Name-2”, where Name-1 and Name-2 are their names in proper order.
"""
str1=str(input())
str2=str(input())
reversestr1=str1[::-1]
reversestr2=str2[::-1]
print(f'{reversestr1} weds {reversestr2}')
