"""
Karishma and her father started a shop for selling market goods to the customers. But the father doesn't know how to do business, but Karishma does. 
She explained how one can buy goods at a cheaper price and market to the customers and make them buy the products.

While explaing to her father, she mentioned three things...

The 'material price', 'selling price/sales price of the material'

Since each day is important, calculate the 'net profit of 28 days' of each profit/loss
"""

x=float(input())
y=float(input())
z=float(input())
if x>y:
    p=(x-y)*z
    print("Total Loss Amount = "+str(p))
elif x==y:
    print("No Profit No Loss!!!")
elif x<y:
    a=(y-x)*z
    print("Total Profit = "+str(a))
