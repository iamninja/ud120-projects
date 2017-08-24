""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    """Docstring"""

    max_val = max(arr)
    min_val = min(arr)
    if max_val == min_val:
        print("All values are the same. No need to rescale")
        return

    for idx, value in enumerate(arr):
        arr[idx] = (value - min_val) / (max_val - min_val)

    return arr

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))
