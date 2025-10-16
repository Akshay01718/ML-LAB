import numpy as np

arr=np.arange(21)
print("Original array:",arr)

even_num=arr[arr%2==0]
print("Even Numbers:",even_num)

greater_than_10=arr[arr>10]
print("Greater than 10:",greater_than_10)

arr[arr%5==0]=-1
print("Replacing multiple of 5 with -1:",arr)