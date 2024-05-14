# -*- coding: utf-8 -*-
"""lvadsusr_193_pred_clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nxjK1dbAg5Jx-zJK7RwEkOBjjJOingoI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import warnings
from sklearn.metrics import silhouette_score
warnings.filterwarnings("ignore")

df=pd.read_csv('/content/customer_segmentation.csv')

df.head(4)

df.isnull().sum()

df['Income'] = df['Income'].fillna(df['Income'].mean())

df.head(2)

df.dtypes

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['Education'] = le.fit_transform(df['Education'])
df['Marital_Status'] = le.fit_transform(df['Marital_Status'])

df.head(2)

df.dtypes

df.drop(columns=['Dt_Customer'], inplace=True)

df.dtypes

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 10))
sns.heatmap(df.corr(), annot=True)
plt.show()

wcss = []

for i in range(1, 11):
  kmeans = KMeans(n_clusters=i, random_state=2)
  kmeans.fit(df)
  wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Graph')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Choose the optimal number of clusters based on the elbow graph
num_clusters = 3

kmeans = KMeans(n_clusters=num_clusters, random_state=2)
kmeans.fit(df)

df['Cluster'] = kmeans.labels_

df.head()

kmeans = KMeans(n_clusters=3, random_state=2)
kmeans.fit(df)
df['Cluster'] = kmeans.labels_
print(df.head())

num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', n_init=10, max_iter=200, tol=0.0001, random_state=42)
Y=kmeans.fit_predict(df)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
df_2d = pca.fit_transform(df)


plt.scatter(df_2d[:, 0], df_2d[:, 1], c=df['Cluster'], s=50, cmap="viridis", alpha=0.8)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='o', s=110, label="Centroids")
plt.title("K-Means Clustering")
plt.legend()
plt.show()

silhouette_score(df, labels)