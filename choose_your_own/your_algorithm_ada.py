#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")

# Set block=False to continue the script after show
plt.show(block=False)
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn import ensemble
from sklearn.metrics import accuracy_score
from time import time

clf = ensemble.AdaBoostClassifier(learning_rate=2, n_estimators=20)
print("Begin training...")
t0 = time()
clf.fit(features_train, labels_train)
print("Classifier trained in: ", time() - t0, "s")

print("Make predictions...")
t1 = time()
pred = clf.predict(features_test)
print("Predictions made in: ", time() - t1, "s")

acc = accuracy_score(pred, labels_test)
print("Accuracy is: ", acc)

try:
    prettyPicture(clf, features_test, labels_test)
    # show() again to prevent python from closing it at the end of script
    plt.show()
except NameError:
    pass
