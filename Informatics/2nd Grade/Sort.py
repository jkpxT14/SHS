import random

def insertionSort(data):
    pass
def bubbleSort(data):
    pass

def quickSort(data):
    if len(data)<=1:
        return data
    less, equal, greater = [], [], []
    pivot=data[0]
    for d in data:
        if d<pivot:
            less.append(d)
        elif d==pivot:
            equal.append(d)
        else:
            greater.append(d)
    return quickSort(less)+equal+quickSort(greater)

x=list(range(1, 1000))
random.shuffle(x)
data=x[:40]
print(quickSort(data))