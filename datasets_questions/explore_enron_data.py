#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# Number of persons
print("The total number of persons is:", len(enron_data))

# Number of features per person
print("The total of features per person is:", len(enron_data[list(enron_data.keys())[0]]))

# Find POIs
#print("The following are the POIs in dataset,")
numberOfPOIs = 0
listOfPOIs = []
for name, features in enron_data.items():
    if (features['poi'] == 1):
        numberOfPOIs += 1
        #print(name)
        listOfPOIs.append(name)
print("There are", numberOfPOIs, "POIs in the dataset.")

names = []
with open('../final_project/poi_names.txt') as f:
    names = f.read().splitlines()
# Clean name list
names = names[2:]
for i, name in enumerate(names):
    names[i] = list(map(str.strip, name[4:].upper().split(','))).sort()
for i, poi in enumerate(listOfPOIs):
    listOfPOIs[i] = poi.split(' ')
    listOfPOIs[i] = [j for j in listOfPOIs[i] if len(j)>2].sort()
#print(listOfPOIs)
#print(names)
#mathches = 0
#for name in names:
#    if name in listOfPOIs:
#        matches += 1
print("The number of POIs in total: ", len(names))
print("The features available are: ", enron_data[list(enron_data.keys())[0]])
print("The total value of stock belonging to James Prentice is:", enron_data['PRENTICE JAMES']['total_stock_value'])
print("The number of emails from Wesley Colwell to POIs is:", enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print("The value of stock options exercised by Jeffrey K Skilling is:", enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print("Total payments Lay:", enron_data['LAY KENNETH L']['total_payments'])
print("Total payments Skilling:", enron_data['SKILLING JEFFREY K']['total_payments'])
print("Total payments Fastow:", enron_data['FASTOW ANDREW S']['total_payments'])
knownSalary = 0
knownEmail = 0
unknownPayments = 0
unknownPOIPayments = 0
totalPOIs = 0
for name, features in enron_data.items():
    if features['salary'] != 'NaN':
        knownSalary += 1
    if features['email_address'] != 'NaN':
        knownEmail += 1
    if features['total_payments'] == 'NaN':
        unknownPayments += 1
    if features['poi']:
        totalPOIs += 1
        if features['total_payments'] == 'NaN':
            unknownPOIPayments += 1
print("Known salaries:", knownSalary)
print("Known emails:", knownEmail)
print("Unknown total payements:", unknownPayments)
print("The unknown payments percentage is:", round(unknownPayments/len(enron_data), 4)*100)
print("Uknown total payments of POIs:", unknownPOIPayments)
print("Then uknown payement percentage of POIs is:", round(unknownPOIPayments/len(enron_data), 4)*100)
