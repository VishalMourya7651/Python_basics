# test_scikit_learn.py

from sklearn.linear_model import LinearRegression
import numpy as np

# sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # y = 2 * x

# create and train model
model = LinearRegression()
model.fit(X, y)

# test prediction
print("Prediction for 6:", model.predict([[16]]))
