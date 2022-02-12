"""
An online food delivery app gives 10% discount on orders above ₹300. Ask the user for order cost and estimate the total bill and print it.
"""

n=float(input())
if n>300:
    p=n-(n*10/100)
    print(p)
else:
    print(n)
