# ---------------------------------------------
# 🌳 Decision Tree Classifier: Buy Computer Data
# ---------------------------------------------

# Step 1: Import the required libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Step 2: Load the dataset
data = pd.read_csv("D:\\ML LAB\\exp9\\Buy_Computer.csv")

# Step 3: Convert all text data (like 'Yes'/'No') into numbers
# This helps the Decision Tree understand the data
data_encoded = data.apply(lambda col: pd.factorize(col)[0])

# Step 4: Split into input (X) and output (y)
X = data_encoded.drop(columns=["Buy_Computer"])   # Features: Age, Income, Student, Credit_rating
y = data_encoded["Buy_Computer"]                    # Target: Whether they buy or not

# Step 5: Create and train the Decision Tree model
model = DecisionTreeClassifier(criterion="entropy")  # Using 'entropy' for information gain
model.fit(X, y)

# Step 6: Visualize the Decision Tree
plt.figure(figsize=(10, 6))
plot_tree(model,
          feature_names=X.columns,   # Column names as feature labels
          class_names=["No", "Yes"], # Output labels
          filled=True,               # Fill colors for clarity
          rounded=True,              # Rounded edges for better look
          fontsize=10)
plt.title("Decision Tree for Buying a Computer")
plt.show()
