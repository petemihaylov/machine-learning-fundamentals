import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# collecting data
data = pd.read_csv("abalone.data")
print(data.head())

# converting the data into a numerical one

le = preprocessing.LabelEncoder()
sex = le.fit_transform(list(data["sex"]))
length = le.fit_transform(list(data["length"]))
diameter = le.fit_transform(list(data["diameter"]))
height = le.fit_transform(list(data["height"]))
whole_weight = le.fit_transform(list(data["whole_weight"]))
shucked_weight = le.fit_transform(list(data["shucked_weight"]))
viscera_weight = le.fit_transform(list(data["viscera_weight"]))
shell_weight = le.fit_transform(list(data['shell_weight']))
ring = le.fit_transform(list(data['rings']))
