# -*- coding: utf-8 -*-
"""lvadsusr_193_pred_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hRNr0cvQchDvlmonm0R5LhHpGr83ZVSm
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
le=LabelEncoder()
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report, f1_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBClassifier
from sklearn.ensemble import AdaBoostRegressor
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression,LinearRegression
from xgboost import XGBRegressor

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report,r2_score,mean_squared_error

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("/content/Fare prediction.csv")
df.head(10)

df.shape

df.info()

df.describe(include='all')

df.dtypes

df.isnull().sum()

df.drop(['key', 'pickup_datetime'], axis=1, inplace=True)

df.columns

num = df.select_dtypes(include=['float64','int64']).columns
correlation_matrix = df[num].corr()
print(correlation_matrix)

sns.heatmap(correlation_matrix,annot=True)

for i in range(len(num)):
  for j in range(i+1,len(num)):
    sns.scatterplot(data=df,x=num[i],y=num[j])
    plt.title(f"Scatter plot between {num[i]} and {num[j]}")
    plt.xlabel(f"{num[i]}")
    plt.ylabel(f"{num[j]}")
    plt.show()

df.dtypes

df.duplicated().sum()

df.drop_duplicates(inplace=True)

df.duplicated().sum()

d = df
X = d.drop(columns=['fare_amount'])
y = d['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = MinMaxScaler()

X_train=pd.DataFrame(scaler.fit_transform(X_train[list(X.columns)]),
                                    columns=X.columns)
X_test=pd.DataFrame(scaler.transform(X_test[list(X.columns)]),
                                    columns=X.columns)

df.isnull().sum()
df.head(2)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
print("Mean Squared Error: ",mse)
rmse = mean_squared_error(y_test,y_pred,squared=False)
print("Root Mean Squared Error: ",rmse)
r2_s = r2_score(y_test,y_pred)
print("R2 Score",r2_s)