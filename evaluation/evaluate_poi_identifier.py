#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn import tree, metrics, model_selection
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson13_keys.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
predictions = clf.predict(features_test)
predictions_fake = [0.] * 29
acc = metrics.accuracy_score(labels_test, predictions)
acc_fake = metrics.accuracy_score(labels_test, predictions_fake)

print(sum(predictions), "poi in", len(predictions), "people. Accuracy:", acc)
print(sum(predictions_fake), "poi in", len(predictions_fake), "people. Accuracy_fake:", acc_fake)

cnt_tp = 0
for i, val in enumerate(predictions):
    if predictions[i] == 1 and labels_test[i] == 1:
        cnt_tp += 1
print("Found", cnt_tp, "true positives.")

prec = metrics.precision_score(labels_test,predictions)
recall = metrics.recall_score(labels_test, predictions)

print("Precision is:", prec, "Recall is:", recall)
