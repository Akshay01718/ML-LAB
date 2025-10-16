import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

#single linera regression
print("Single Linear Regression (TV vs Sales)")
advertising_df = pd.read_csv("LAB/exp7/advertising.csv")
X_single = advertising_df[['TV']]
y_single = advertising_df['Sales']

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_single, y_single, test_size=0.2, random_state=42)

model_single = LinearRegression()
model_single.fit(X_train_s, y_train_s)
y_pred_s = model_single.predict(X_test_s)

r2_single = r2_score(y_test_s, y_pred_s)
print("R² Score (Single Linear):", r2_single)

# Plot
plt.figure(figsize=(6, 4))
plt.scatter(X_test_s, y_test_s, color='blue', label='Actual')
plt.plot(X_test_s, y_pred_s, color='red', label='Prediction')
plt.title("Single Linear Regression (TV vs Sales)")
plt.xlabel("TV Advertising")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#multiple linear regression
print("\nMultiple Linear Regression (Boston Housing) ")
boston_df = pd.read_csv("LAB/exp7/Boston.csv")
if 'Unnamed: 0' in boston_df.columns:
    boston_df = boston_df.drop(columns=['Unnamed: 0'])

X_multi = boston_df.drop(columns=['medv'])
y_multi = boston_df['medv']

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)
y_pred_m = model_multi.predict(X_test_m)

r2_multi = r2_score(y_test_m, y_pred_m)
print("R² Score (Multiple Linear):", r2_multi)

# Plot Actual vs Predicted values
plt.figure(figsize=(6, 4))
plt.scatter(y_test_m, y_pred_m, color='purple', edgecolor='k')
plt.plot([y_test_m.min(), y_test_m.max()], [y_test_m.min(), y_test_m.max()], 'r--')
plt.xlabel("Actual medv")
plt.ylabel("Predicted medv")
plt.title("Multiple Linear Regression: Actual vs Predicted")
plt.grid(True)
plt.tight_layout()
plt.show()

'''
#polynomial regression
print("\nPolynomial Regression (Month vs Sales)")
ice_df = pd.read_csv("LAB/exp7/ice_cream1.csv")
X_poly = ice_df[['month']]
y_poly = ice_df['sales']

poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_poly_transformed, y_poly, test_size=0.2, random_state=42)

model_poly = LinearRegression()
model_poly.fit(X_train_p, y_train_p)
y_pred_p = model_poly.predict(X_test_p)

r2_poly = r2_score(y_test_p, y_pred_p)
print("R² Score (Polynomial Regression):", r2_poly)

X_sorted = X_poly.sort_values(by='month')
X_sorted_poly = poly.transform(X_sorted)
y_sorted_pred = model_poly.predict(X_sorted_poly)

plt.figure(figsize=(6, 4))
plt.scatter(X_poly, y_poly, color='green', label='Actual')
plt.plot(X_sorted, y_sorted_pred, color='orange', label='Polynomial Fit')
plt.title("Polynomial Regression (Month vs Ice Cream Sales)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
'''