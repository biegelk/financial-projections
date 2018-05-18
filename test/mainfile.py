import numpy as np
from thing import *

class Utility:
    def __init__(self):
        self.revenues = np.zeros(6)
        self.opexpenses = np.zeros(6)


so = Utility()

adjust(so)

print(so.revenues)
