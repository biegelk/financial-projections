# A pro forma financial statement generator for a utility building
#     a nuclear power plant.
# Author: Katie Biegel
# Last revision: 2018-05-16

# Boolean to enable probabilistic delay (uniform [1,2]*initial estimate)
rand_delay = 1

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

# Simulate plant construction project and return spend profiles
npp = Project(rand_delay)
npp.build_plant()

# Compute project LCOE
npp.get_lcoe()
print("LCOE = ",npp.lcoe,"c/kWh")

# Compute project NPV
npp.get_npv()
print("NPV = $", npp.npv,"M")

ut.finance_project(npp)

ut.refresh_IS(hist)

ut.write_IS_csv()
