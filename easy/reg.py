

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# -------------------------------------------------------
# 1️⃣ SINGLE LINEAR REGRESSION (TV vs Sales)
# -------------------------------------------------------

print("Single Linear Regression: TV vs Sales")

# Load dataset
data = pd.read_csv(r"D:\ML LAB\exp7\advertising.csv")


# Select one feature (TV) and the target (Sales)
X = data[['TV']]
y = data['Sales']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict sales for test data
y_pred = model.predict(X_test)

# Calculate accuracy (R² score)
print("R² Score:", r2_score(y_test, y_pred))

# Plot
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.title("Single Linear Regression (TV vs Sales)")
plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")
plt.legend()
plt.show()


# -------------------------------------------------------
# 2️⃣ MULTIPLE LINEAR REGRESSION (Boston Housing)
# -------------------------------------------------------

print("\nMultiple Linear Regression: Boston Housing Data")

# Load dataset
boston = pd.read_csv(r"D:\ML LAB\exp7\Boston.csv")

# Remove unwanted column (if present)
if 'Unnamed: 0' in boston.columns:
    boston = boston.drop(columns=['Unnamed: 0'])

# Select all columns except 'medv' as input
X = boston.drop(columns=['medv'])
y = boston['medv']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))

# Plot actual vs predicted
plt.scatter(y_test, y_pred, color='purple')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title("Multiple Linear Regression")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.show()


# -------------------------------------------------------
# 3️⃣ POLYNOMIAL REGRESSION (Month vs Ice Cream Sales)
# -------------------------------------------------------

print("\nPolynomial Regression: Month vs Ice Cream Sales")

# Load dataset
ice = pd.read_csv(r"D:\ML LAB\exp7\ice_cream1.csv")

# Select feature and target
X = ice[['Temperature (°C)']]
y = ice['Ice Cream Sales (units)']

# Convert X into polynomial features (x, x²)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))

# Plot
X_sorted = X.sort_values(by='Temperature (°C)')
y_sorted_pred = model.predict(poly.transform(X_sorted))

plt.scatter(X, y, color='green', label='Actual')
plt.plot(X_sorted, y_sorted_pred, color='orange', label='Polynomial Fit')
plt.title("Polynomial Regression (Temperature vs Ice Cream Sales)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales (units)")
plt.legend()
plt.show()
