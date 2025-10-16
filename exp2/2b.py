import numpy as np

arr=np.arange(1,17).reshape(4,4)

second_row=arr[1]
print("Second row:",second_row)

third_col=arr[:,2]
print("Third column:",third_col)

sub_matrix=arr[1:4,1:4]
print("Sub matrix:\n",sub_matrix)

arr[0]=0
print("After replacing:\n",arr)
