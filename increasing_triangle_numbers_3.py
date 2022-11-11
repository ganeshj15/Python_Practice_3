n = 5 # n is required number of rows.
# n = int(input('Enter the number of rows you want')) to get the number of rows from user use this line.
for i in range(n):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()

# O/P pattern
"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""