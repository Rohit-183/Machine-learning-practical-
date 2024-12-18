# -*- coding: utf-8 -*-
"""BE21F03F049_Clusterring.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ghUCDXO8z3YiabpOBV62-JXB_FSL2cvM
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('/content/placement-dataset.csv')

# Select the features for clustering
X = df[['cgpa', 'iq']]

# Determine the optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Perform K-Means clustering
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Visualize the clusters
plt.scatter(X['cgpa'], X['iq'], c=y_kmeans, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.legend()
plt.show()