# ---------------------------------------------------
# 💸 K-Means Clustering on Mall Customers Dataset (with Labels)
# ---------------------------------------------------

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 2: Load dataset
data = pd.read_csv("D:/ML LAB/exp11/Mall_Customers.csv")

# Step 3: Select features (Annual Income & Spending Score)
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Step 4: Create and train K-Means model
kmeans = KMeans(n_clusters=6, random_state=0)
kmeans.fit(X)

# Step 5: Get cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Step 6: Add cluster info to the dataset
data['Cluster'] = labels

# Step 7: Plot clusters with labels
plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green', 'orange', 'purple','brown']

# Plot each cluster separately so each one gets its label in the legend
for i in range(6):
    cluster_points = X[data['Cluster'] == i]
    plt.scatter(
        cluster_points['Annual Income (k$)'],
        cluster_points['Spending Score (1-100)'],
        color=colors[i],
        label=f'Cluster {i+1}',
        s=50,
        alpha=0.7
    )

# Plot centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c='black',
    marker='X',
    s=200,
    label='Centroids'
)

# Titles and labels
plt.title('K-Means Clustering of Mall Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)
plt.show()

# Step 8: Print info
print("📊 Cluster Centers:")
for i, center in enumerate(centroids):
    print(f"Cluster {i+1}: {center}")
