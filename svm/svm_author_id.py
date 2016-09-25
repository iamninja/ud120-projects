#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# reduce data
#features_train = features_train[:round(len(features_train)/100)]
#labels_train = labels_train[:round(len(labels_train)/100)]

clf = SVC(kernel="rbf", C=10000.0)
print("Training classifier...")
t0 = time()
clf.fit(features_train, labels_train)
print("Training time: ", round(time() - t0, 3), "s")

t1 = time()
print("The accuracy \(using score\) is: ", clf.score(features_test, labels_test), ".")
print("Computing accuracy with score took: ", round(time() - t1, 3), "s")

t2 = time()
print("Make predicitons...")
pred = clf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print("The accuracy \(using accuracy_score\) is: ", accuracy, ".")
print("Computing accuracy with accuracy_score took: ", round(time() - t2, 3), "s")

print("10th: ", pred[10])

print("26th: ", pred[26])

print("50th: ", pred[50])

print("# Chris' mails: ", pred.sum())




#########################################################


