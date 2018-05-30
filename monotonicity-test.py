import math as m
import numpy as np
import csv
import os

a = 1
d = 1
f = 1

arange = 2
drange = 10
frange = 2

asamples = 100
dsamples = 100
fsamples = 100

def func(a, d, f):
    return d * m.exp(a*d) - 4 * (1 + f)*d**2 / m.pi**2 * a


results = np.zeros((arange*asamples, drange*dsamples, frange*fsamples))
count_negative = 0

with open('mproof-data.csv', 'w') as pfile:
    writer = csv.writer(pfile, delimiter = ',', quotechar = '\"')
    writer.writerow(["a: " + str(asamples) + " samples on the interval [0," + str(0+arange) + "]"])
    writer.writerow(["d: " + str(dsamples) + " samples on the interval [5," + str(5+drange) + "]"])
    writer.writerow(["f: " + str(fsamples) + " samples on the interval [f," + str(0+frange) + "]"])
    writer.writerow(["a", "d", "f", "df/da"])
    for i in range(arange*asamples):
        for j in range(drange*dsamples):
            for k in range(frange*fsamples):
                results[i, j, k] = func(float(i)/asamples, float(j)/dsamples, float(k)/fsamples)
                writer.writerow(np.hstack(([float(i)/asamples, float(j)/dsamples, float(k)/fsamples], results[i, j, k])))
                if results[i, j, k] < 0:
                    count_negative += 1

print(count_negative)
