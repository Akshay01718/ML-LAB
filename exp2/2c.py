import pandas as pd

emp={
    'Name':["AJ","Ak","AI","AB"],
    'Age':["19","20","21","22"],
    'Dept':["Web","UI","HR","Testing"],
    'Salary':[20000,17000,27000,35000]
}

df=pd.DataFrame(emp)
print(df)

print("First row")
print(df.head(1))

print("Last row")
print(df.tail(1))

avg=df['Salary'].mean()
print("Average Salary:",avg)

df['Bonus']=df['Salary']*0.10
print("Employee data with bonus:")
print(df)

df=df.drop('Dept',axis=1)
print("Deparment dropped")
print(df)

df=df.rename(columns={'Name':'Emp_Name'})
print("Renamed")
print(df)