import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def plot_confusion_matrix(y_true, y_pred, classes):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.show()

def plot_svm_decision_boundary(X, y, model):
    # Only works for 2 features
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500),
                         np.linspace(y_min, y_max, 500))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
plt.title("SVM Decision Boundary")
plt.show()

def svm_classifier(data_path):
    # Load dataset from CSV file
    data = pd.read_csv(data_path)

    # Select only two features for visualization purposes
    X = data.iloc[:, [0, 2]].values   # For example: sepal_length and petal_length
    y = data.iloc[:, -1].values       # species

    # Encode the target variable (if categorical)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    # Create an SVM classifier with linear kernel
    svm = SVC(kernel='linear')

    # Train the classifier on the training data
    svm.fit(X_train, y_train)

    # Predict the labels for the test data
    y_pred = svm.predict(X_test)

    # Calculate and print the accuracy of the classifier
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of the SVM classifier: {accuracy:.4f}")

    # Plot confusion matrix
    plot_confusion_matrix(y_test, y_pred, classes=le.classes_)

    # Plot decision boundary (using the training data for clearer boundaries)
    plot_svm_decision_boundary(X_train, y_train, svm)


if __name__ == "__main__":
    # <-- Set your dataset path here -->
    dataset_path = "/home/cse-ai-05/Desktop/Maria/Iris.csv"  # Change this to your CSV file path

    svm_classifier(dataset_path)
