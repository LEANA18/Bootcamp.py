"""
Following is KTU grading system(in percentage):

Below 40 - F (Fail)
40 to below 55 - P (Pass)
55 to below 60 - D
60 to below 65 - C
65 to below 70 - C+
70 to below 75 - B
75 to below 80 - B+
80 to below 85 - A
85 to below 90 - A+
90 and above - S
Ask user to enter the total marks of the subject, marks she obtained and find the corresponding grade and print it.
"""

total=int(input())
marks=int(input())

if marks>=90:
    print('S')
elif marks>=85 and marks<90:
    print('A+')
elif marks>=80 and marks<85:
    print('A')
elif marks>=75 and marks<80:
    print('B+')
elif marks>=70 and marks<75:
    print('B')
elif marks>=65 and marks<70:
    print('C+')
elif marks>=60 and marks<65:
    print('C')
elif marks>=55 and marks<60:
    print('D')
elif marks>=40 and marks<55:
    print('P')
elif marks<40:
    print('F')
