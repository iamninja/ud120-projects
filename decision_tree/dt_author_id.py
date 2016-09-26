#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier(min_samples_split=40)
print("Begin training...")
t0 = time()
clf.fit(features_train, labels_train)
print("DT trained in: ", (time() - t0), "s")

print("Make predictions...")
t1 = time()
pred = clf.predict(features_test)
print("Predictions made in: ", time() - t1, "s")

acc = accuracy_score(pred, labels_test)
print("Accuracy score is: ", acc)

print("The total number of features is: ", len(features_train[0]))
#########################################################


