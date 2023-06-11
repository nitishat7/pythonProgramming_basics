# read write in csv

import csv
with open("details.csv") as f:
    data = csv.reader(f)
    for i in data:
        print(i)


# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,22])
# print(a)
# print(type(a))


