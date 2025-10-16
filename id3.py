import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv("LAB/exp10/Buy_Computer.csv")
print("Columns in dataset:", df.columns.tolist())

df_encoded = df.apply(lambda col: pd.factorize(col)[0])
X = df_encoded.drop("Buy_Computer", axis=1)
y = df_encoded["Buy_Computer"]

clf = DecisionTreeClassifier(criterion="entropy")
clf.fit(X, y)

plt.figure(figsize=(12,8))
plot_tree(clf,
          feature_names=list(X.columns),
          class_names=["No","Yes"],
          filled=True,
          rounded=True,
          fontsize=10)
plt.show()
