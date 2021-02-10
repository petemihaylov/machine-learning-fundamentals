import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# collecting data
data = pd.read_csv("car.data.txt")
print(data.head())

# converting the data into a numerical one

le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
persons = le.fit_transform(list(data["persons"]))
door = le.fit_transform(list(data["door"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

# zip convert the chunk of data to list
x = list(zip(buying, maint, persons, door, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test =  sklearn.model_selection.train_test_split(x, y, test_size=0.1)


