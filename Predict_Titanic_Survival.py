import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')

# Update sex column to numerical
#passengers["Sex"] = np.where((passengers["Sex"] == "female"), 1, 0)
passengers["Sex"] = passengers["Sex"].map({"female":1, "male":0})

# Fill the nan values in the age column
mean_age = passengers["Age"].mean()
passengers["Age"].fillna(mean_age, inplace=True)

# Create a first class column
passengers["FirstClass"] = passengers["Pclass"].apply(lambda x:1 if x == 1 else 0)
#passengers["FirstClass"] = passengers["Pclass"].map({1:1})
#passengers["FirstClass"].fillna(0, inplace=True)

# Create a second class column
passengers["SecondClass"] = passengers["Pclass"].apply(lambda x:1 if x == 2 else 0)

# Select the desired features
features = passengers[["Sex", "Age", "FirstClass", "SecondClass"]]
survival = passengers["Survived"]

# Perform train, test, split
features_train, features_test, survival_train, survival_test = train_test_split(features, survival, test_size = 0.25)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)

# Create and train the model
model = LogisticRegression()
model.fit(features_train, survival_train)

# Score the model on the train data
print(model.score(features_train, survival_train))

# Score the model on the test data
print(model.score(features_test, survival_test))

# Analyze the coefficients
#print(model.coef_)
print(list(zip(["Sex", "Age", "FirstClass", "SecondClass"], model.coef_[0])))

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([1.0,25.0,1.0,0.0])

# Combine passenger arrays
#sample_passengers = np.row_stack((Jack, Rose, You))
sample_passengers = np.array([Jack, Rose, You])
print(sample_passengers)

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
print(model.predict(sample_passengers))
print(model.predict_proba(sample_passengers))
