import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report


data = load_breast_cancer()
data_normalized = preprocessing.normalize(data["data"], norm = "l2")
features_train, features_test, labels_train, labels_test = train_test_split(data_normalized, data["target"], test_size = 0.25, random_state = 23)
model = LogisticRegression()
#print(data["data"])
#print(labels_train)
model.fit(features_train, labels_train)
cancer_predictions = model.predict(features_test)
print(classification_report(labels_test, cancer_predictions))

coefficients = model.coef_
coefficients = coefficients.tolist()[0]
plt.bar(range(len(data["feature_names"])), coefficients)
plt.xticks(range(len(data["feature_names"])),data["feature_names"], rotation='vertical')
plt.show()