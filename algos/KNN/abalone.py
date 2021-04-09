import sklearn
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# collecting data
data = pd.read_csv("abalone.data")
print(data.tail())

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
rings = le.fit_transform(list(data['rings']))

predict = "rings"

# zip convert the chunk of data to list
x = list(zip(sex, length, diameter, height, whole_weight, shucked_weight, viscera_weight, shell_weight))
y = list(rings)


knn = KNeighborsClassifier(n_neighbors=33)
x_train, x_test, y_train, y_test =  sklearn.model_selection.train_test_split(x, y, test_size=0.1)

knn.fit(x_train, y_train)

predicted = knn.predict(x_test)
acc = sklearn.metrics.accuracy_score(y_test, predicted)

print("Accuracy: ", acc )

for x in range( len(predicted)):
    print("Predicted: ", predicted[x], "Data: ", x_test[x], "Actual: ", y_test[x])

