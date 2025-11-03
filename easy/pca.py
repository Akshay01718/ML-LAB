# ---------------------------------------------
# 🌸 PCA (Principal Component Analysis) on Iris Dataset
# ---------------------------------------------

# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 2: Load the dataset
data = pd.read_csv("D:\\ML LAB\\exp10\\Iris.csv")

# Step 3: Separate features (X) and target (y)
X = data.drop(columns=['Species'])  # All columns except the last (features)
y = data['Species']  # Last column (species name)

# Step 4: Standardize the data (very important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Apply PCA to reduce dimensions from 4 → 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Step 6: Plot the two principal components
plt.figure(figsize=(8, 6))
for species in np.unique(y):
    plt.scatter(
        X_pca[y == species, 0],
        X_pca[y == species, 1],
        label=species,
        alpha=0.7
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA on Iris Dataset")
plt.legend()
plt.grid(True)
plt.show()

# Step 7: Show how much variance (information) each component holds
print("Explained variance ratio:", pca.explained_variance_ratio_)
