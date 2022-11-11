n = 5 # n is required number of rows.
# n = int(input('Enter the number of rows you want')) to get the number of rows from user use this line.

# this problem can be divided into three triangles like 1. increasing triangle pattern printing spaces 2. two decreasing triangle patterns printing *

for i in range(n):
    for j in range(i):
        print(" ", end= " ")
    for k in range(i,n):
        print("*",end= " ")
    for l in range(i+1,n):
        print("*",end= " ")
    print()

# O/P Pattern
"""
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""