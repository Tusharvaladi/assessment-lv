# -*- coding: utf-8 -*-
"""lvadsusr_193_pred_anomaly.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dYSwVTqumhHjwRa2U-h6ET3ShXd0Pwe9
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

df = pd.read_csv("/content/anomaly_train.csv")

df.head()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])

model = IsolationForest(n_estimators=100, contamination=0.1)

model.fit(df[['Amount', 'Location']])
predictions = model.predict(df[['Amount', 'Location']])


anomaly_indices = np.where(predictions == -1)[0]

plt.figure(figsize=(10, 6))

plt.scatter(df.loc[predictions == 1, 'Amount'], df.loc[predictions == 1, 'Location'], color='blue', label='Normal')

plt.scatter(df.loc[predictions == -1, 'Amount'], df.loc[predictions == -1, 'Location'], color='red', label='Anomaly')

plt.xlabel('Amount')
plt.ylabel('Location')
plt.legend()
plt.show()