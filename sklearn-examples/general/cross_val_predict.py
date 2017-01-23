from sklearn import datasets, linear_model
# from sklearn.model_selection import cross_val_predict#并不是model_selection
from sklearn.cross_validation import cross_val_predict
from matplotlib import pyplot as plt
import numpy as np

lr = linear_model.LinearRegression()
boston = datasets.load_boston()

X= boston.data
y= boston.target
print("x is-----")
print(np.shape(X))
print(X)
print('y is ------')
print(np.shape(y))
print('y min: {0}; max: {1}'.format(y.min(),y.max()))
print(y)

predicted = cross_val_predict(lr, X, y, cv=10)
print("predicted-----")
print(np.shape(predicted))
print('predicted min: {0}; max: {1}'.format(predicted.min(),predicted.max()))
print(predicted)

fig,ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(),y.max()],[y.min(),y.max()],'k--',lw=4)
ax.set_xlabel("measured")
ax.set_ylabel("predicted")
plt.show()