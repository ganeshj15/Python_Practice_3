n = 5

# This problem may be divided into printing pyramid with upward apex and then printing pyramid with downward apex.
for i in range(n-1):
    for j in range(i+1,n):# decreasing triangle printing spaces
        print(" ",end= " ")
    for k in range(i): #  first increasing triangle printing "*"
        print('*',end= " ")
    for j in range(i+1): # second increasing triangle printing "*"
        print('*',end= " ")
    print()
for i in range(n):
    for j in range(i):
        print(" ", end= " ")
    for j in range(i,n):
        print("*",end= " ")
    for j in range(i+1,n):
        print("*",end= " ")
    print()

# O/P Pattern
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""