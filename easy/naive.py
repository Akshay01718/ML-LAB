# ---------------------------------------------
# 🧠 Loan Approval Prediction using Naive Bayes
# ---------------------------------------------

# Step 1: Import the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Step 2: Load the dataset
data = pd.read_csv("D:\\ML LAB\\exp8\\loan.csv")   # Make sure 'loan.csv' is in the same folder as this file

# Step 3: Clean and prepare the data
# Remove the Loan_ID column (it doesn’t help in prediction)
data = data.drop('Loan_ID', axis=1)

# Convert Loan_Status from 'Y'/'N' to 1/0
data['Loan_Status'] = data['Loan_Status'].map({'Y': 1, 'N': 0})

# Convert text columns (like Gender, Education, etc.) into numbers
data = pd.get_dummies(data, drop_first=True)


# Step 4: Split into features and target
X = data.drop('Loan_Status', axis=1)  # Inputs
y = data['Loan_Status']               # Output

# Step 5: Split into training and testing sets
# 70% data for training, 30% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)


# Step 6: Create and train the Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Check performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Step 9: Print results
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
