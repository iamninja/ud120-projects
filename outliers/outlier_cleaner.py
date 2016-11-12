#!/usr/bin/python
import operator


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = list(map(operator.sub, net_worths, predictions))
    errors = list(map(operator.abs, errors))
    data = [ages, net_worths, errors]
    # transpose data
    data = [[row[i] for row in data] for i in range(len(predictions))]
    #data = zip(*data)
    # sort data
    data.sort(key=lambda x: x[2])
    # filter data
    cleaned_data = data[0:int(len(data)*9/10)]
    return cleaned_data


