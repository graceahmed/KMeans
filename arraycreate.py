#This code will convert a csv of strings to a numpy array of floats (numbers)
import numpy as np

A = ([])
line_school = open("myfile.csv", "rb")
for line in line_school:
    array = [i.strip() for i in line.split(',')]
    print array
    A.append(array)
B = np.array(A)
X = B.astype(np.float) 

# the variable X will be used in the k_means_class.py
# e.g kmeans.fit(X)
