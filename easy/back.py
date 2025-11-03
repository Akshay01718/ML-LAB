import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"D:/ML LAB/exp10/Iris.csv")


X = data.drop(columns=['Species'])
y = data['Species']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=1
)


mlp = MLPClassifier(
    random_state=1,
    max_iter=1000,
    hidden_layer_sizes=(100,),
    solver='adam',
    learning_rate_init=0.001,
    batch_size=50
)

mlp.fit(X_train, y_train)


y_pred = mlp.predict(X_test)

confusion_mtx = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion_mtx)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


plt.figure(figsize=(8, 5))
plt.plot(mlp.loss_curve_, color='blue', linewidth=2)
plt.title("MLP Learning Progress (Loss Curve)")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()