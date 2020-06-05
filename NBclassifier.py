from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


iris = datasets.load_iris()  # Loads the data from sklearn's datasets.

X_train, X_test, y_train, y_test = train_test_split (iris.data, iris.target, test_size = 0.2)   # Splits 80% training 20% testing

model = GaussianNB()

model.fit(X_train, y_train)     # Trains the model

predicts = model.predict(X_test)    # Applies the calculated probabilities to find 

print(metrics.accuracy_score(predicts, y_test)*100)   # Grades the model based on performance.
