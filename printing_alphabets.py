n = 5 # n is required number of rows.
# n = int(input('Enter the number of rows you want')) to get the number of rows from user use this line.

for i in range(n):
    l = 65 # ASCII value of 'A' is 65 which can be checked by ord() function. So we started with 65
    for j in range(i+1):
        print(chr(l), end= " ")
        l += 1
    print()

# O/P Pattern
"""
A 
A B 
A B C 
A B C D 
A B C D E 
"""