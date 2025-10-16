import pandas as pd

df=pd.read_csv("./employees.csv")

df=df[df["salary"]>20000]

df=df.sort_values(by="salary",ascending=False)

df.to_csv("filtered_employees.csv")
