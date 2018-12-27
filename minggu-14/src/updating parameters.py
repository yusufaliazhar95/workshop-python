import numpy as np
from sklearn.svm import SVC

rng = np.random.RandomState(0)
X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)

clf = SVC()
clf.set_params(kernel='linear').fit(X, y)  




clf.predict(X_test)


clf.set_params(kernel='rbf', gamma='scale').fit(X, y)  




clf.predict(X_test)