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

is_cash_shortage = np.zeros(num_iterations)
cash_shortage = np.zeros((num_iterations, time_horizon+hist))

for i in range(num_iterations):
    # Create utility object, calling selected financial data profile
    # Currently available options: "so" and "scg"
    ut = Utility("so", time_horizon, hist)
    ut.initialize_IS()
    ut.initialize_CFS()

    # Simulate plant construction project and return spend profiles
    npp = Project()
    npp.delay_project()
    npp.build_plant()

    # Compute project LCOE
    npp.get_lcoe()

    # Compute project NPV
    npp.get_npv()

    ut.incorporate_project(npp)

    ut.refresh_IS(hist)
    ut.refresh_CFS(npp, npp.duration)

    # Track outcomes
    costs[i] = npp.total_cost
    durations[i] = npp.duration
    npvs[i] = npp.npv
    lcoes[i] = npp.lcoe

    for j in range(time_horizon + hist):
        if ut.fcf[j] <= 0.0:
            is_cash_shortage[i] += 1
            cash_shortage[i,j] = ut.fcf[j]


print("average cost = ", np.mean(costs))
print("average duration = ", np.mean(durations))
print("average npv = ", np.mean(npvs))
print("average lcoe = ", np.mean(lcoes))
print("Average cash shortage years within forecast period = ", np.sum(is_cash_shortage) / num_iterations)
print("Std. dev cash shortage years w/in forecast period = ", np.std(is_cash_shortage))

total_cash_shortage = np.zeros(num_iterations)
for i in range(num_iterations):
    total_cash_shortage[i] = np.sum(cash_shortage[i,:])
print("Average total cash shortage within forecast period = ", np.mean(total_cash_shortage))
print("Std. dev total cash shortage within forecast period = ", np.std(total_cash_shortage))

