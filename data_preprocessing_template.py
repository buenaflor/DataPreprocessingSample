# Data Preprocessing Template

# Importing the libraries

# Contains mathematical tools
import numpy as np

# Helps us plot nice chart
import matplotlib.pyplot as plt

# Best library for importing and managing data sets
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('Data.csv')

# Matrix of features
X = dataset.iloc[:, :-1].values

# Dependent variable vector
y = dataset.iloc[:, 3].values


# Taking care of missing data

# Imputer class will allow us to take care of the missing data
from sklearn.preprocessing import Imputer

# Mean is the default value for strategy
# Mean of the column -> mean of the features
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# Not 2, 3 -> Upper bound is excluded
imputer = imputer.fit(X[:, 1:3])

# Transform replaces the missing data with the mean
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

# Specify which column we want to onehotencode
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# To Encode the Purchased, we don't need hotencoder since we knows
# it's the dependent variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# Splitting the dataset into the Training Set and Test Set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)





