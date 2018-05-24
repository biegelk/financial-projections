# A pro forma financial statement generator for a utility building a nuclear power plant.
# Author: Katie Biegel
# Last revision: 2018-05-23

import numpy as np
import matplotlib.pyplot as plt
from random import *
from math import *
import csv

# Custom modules
from projections import *
from build import *
from constants import *
from utility import *

# Create utility object, calling selected financial data profile
# Currently available options: "so" and "scg"
ut = Utility("so", time_horizon, hist)
ut.initialize_IS()
ut.initialize_CFS()

# Simulate plant construction project and return spend profiles
npp = Project()
npp.build_plant()

print(npp.duration)

# Compute project LCOE
npp.get_lcoe()
print("LCOE = ",npp.lcoe,"c/kWh")

# Compute project NPV
npp.get_npv()
print("NPV = $", npp.npv,"M")

ut.incorporate_project(npp)

ut.refresh_IS(hist)
ut.refresh_CFS(npp, npp.duration)

ut.write_csv()
