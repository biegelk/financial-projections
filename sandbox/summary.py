import numpy as np

def summary_mover(smlist, *args):
    for arg in args:
        smlist += arg
    return smlist


ebitda = np.zeros(5)
a = np.array([1, 1, 1, 1, 1])
b = np.array([2, 2, 2, 2, 2])
c = np.array([5, 5, 5, 5, 5])

ebitda = summary_mover(ebitda, a, b, c*(-1))
print(ebitda)
