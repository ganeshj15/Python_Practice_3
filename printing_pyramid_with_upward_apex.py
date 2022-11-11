n = 5 # n is required number of rows.
# n = int(input('Enter the number of rows you want')) to get the number of rows from user use this line.

# this problem can be divided into three triangles like 1. decreasing triangle pattern printing spaces 2. two increasing triangle patterns printing *

for i in range(n):
    for j in range(i+1,n):# decreasing triangle printing spaces
        print(" ",end= " ")
    for k in range(i): #  first increasing triangle printing "*"
        print('*',end= " ")
    for j in range(i+1): # second increasing triangle printing "*"
        print('*',end= " ")
    print()

#O/P Pattern
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""