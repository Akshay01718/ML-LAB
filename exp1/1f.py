import numpy as np

row1=int(input("Enter the number of rows of first matrix:"))
col1=int(input("Enter the number of colums of first matrix:"))

m1,m2=[],[]

for i in range(row1):
    temp=[]
    for j in range(col1):
        value=int(input("Enter the values of matrix 1:"))
        temp.append(value)
    m1.append(temp)
        
    
print(m1)

row2=int(input("Enter the number of rows of second matrix:"))
col2=int(input("Enter the number of colums of second matrix:"))

for i in range(row2):
    temp=[]
    for j in range(col2):
        value=int(input("Enter the values of matrix 2:"))
        temp.append(value)
    m2.append(temp)
        
    
print(m2)

sum1=np.add(m1,m2)

print(sum1)