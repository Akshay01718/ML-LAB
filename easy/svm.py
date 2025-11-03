import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


data = pd.read_csv(r"D:/ML LAB/exp10/Iris.csv")


X = data.drop(columns=['Species'])
y = data['Species']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


svm = SVC(kernel='linear')  # Try 'rbf', 'poly', etc.
svm.fit(X_train, y_train)


y_pred = svm.predict(X_test)

print("Support Vectors:")
print(svm.support_vectors_)


cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix (SVM):")
print(cm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=y.unique())
disp.plot()
plt.show()

accuracy = accuracy_score(y_test, y_pred)
print("\nClassifier Accuracy:", accuracy * 100, '%')
