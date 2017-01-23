import numpy as np

from sklearn.utils import check_random_state
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LinearRegression

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

n=100
x = np.arange(n)
print('x is:')
print(x)
rs = check_random_state(0)
# print(rs)
# print(rs.randint(-50,50,size=(10,)))
y = rs.randint(-50,50,size=(n,)) + 50.0 * np.log(1+np.arange(n))
print('y is:')
print(y)

ir = IsotonicRegression()
y_ir = ir.fit_transform(x,y)
print('y of Isotonic regression is:')
print(y_ir)

lr=LinearRegression()
lr.fit(x[:,np.newaxis], y)
y_lr = lr.predict(x[:,np.newaxis])
print('y of linear regression os:')
print(y_lr)

segments = [ [[i,y[i]],[i,y_ir[i]]] for i in range(n)]

lc = LineCollection(segments, zorder=0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(0.5*np.ones(n))

fig = plt.figure()
plt.plot(x,y,'r.',markersize=12)
plt.plot(x,y_ir,'g.-',markersize=12)
plt.plot(x,y_lr,'b-')
plt.gca().add_collection(lc)
plt.legend(('data','Isonotic Fit','Linear Fit'),loc='lower right')
plt.title('Isonotic regression')
plt.show()