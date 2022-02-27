"""
You are given a list of 10 numbers. You have to print out the number of above average numbers in the list.
Above average numbers are the numbers which are greater than the average of the numbers in the list.
"""
a = list(map(int,input().split()))
sum=0
for i in a:
    sum=sum+i
avg=sum/10
b=[]
for i in a:
    if i > avg:
        b.append(i)
print(len(b))
