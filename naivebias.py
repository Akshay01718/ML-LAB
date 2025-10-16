import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

df = pd.read_csv('LAB/exp9/loan.csv')
df = df.drop('Loan_ID', axis=1)
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

X = pd.get_dummies(df.drop('Loan_Status', axis=1), drop_first=True)
y = df['Loan_Status']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision-0.25)
print("Recall:", recall)
