# A pro forma financial statement generator for a utility building
#     a nuclear power plant.
# Author: Katie Biegel
# Last revision: 2018-05-16

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

num_iterations = 1000

npvs = np.zeros(num_iterations)
lcoes = np.zeros(num_iterations)
costs = np.zeros(num_iterations)
durations = np.zeros(num_iterations)

for i in range(num_iterations):
    # Create utility object, calling selected financial data profile
    # Currently available options: "so" and "scg"
    ut = Utility("so", time_horizon, hist)
    ut.initialize_IS()

    # Simulate plant construction project and return spend profiles
    npp = Project()
    npp.build_plant()

    # Compute project LCOE
    npp.get_lcoe()

    # Compute project NPV
    npp.get_npv()

    ut.finance_project(npp)

    ut.refresh_IS(hist)

    # Track outcomes
    costs[i] = npp.total_cost
    durations[i] = npp.duration
    npvs[i] = npp.npv
    lcoes[i] = npp.lcoe


print("average cost = ", np.mean(costs))
print("average duration = ", np.mean(durations))
print("average npv = ", np.mean(npvs))
print("average lcoe = ", np.mean(lcoes))
