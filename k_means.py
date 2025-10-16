import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("LAB/Mall_Customers.csv")

X = df[['Annual Income (k$)', 'Spending Score (1–100)']].values

kmeans = KMeans(n_clusters=8, n_init=10, random_state=0)
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

for i, centroid in enumerate(centroids):
    print(f'Centroid {i + 1}: {centroid}')

colors = ['blue', 'orange', 'black', 'green', 'purple', 'red', 'yellow', 'pink']
cluster_colors = [colors[label] for label in labels]

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=cluster_colors, s=50, alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='red', label='Centroids')

for i, color in enumerate(colors[:len(centroids)]):
    plt.scatter([], [], c=color, label=f'Cluster {i + 1}')

# Labels
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1–100)')
plt.legend()
plt.show()
