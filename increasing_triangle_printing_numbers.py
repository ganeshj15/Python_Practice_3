n = 5 # n is required number of rows.
# n = int(input('Enter the number of rows you want')) to get the number of rows from user use this line.
for i in range(n):
    for j in range(i+1):
        print(i+1,end = " ")
    print()

# O/P pattern
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""