# A pro forma financial statement generator for a utility building
#     a nuclear power plant.
# Author: Katie Biegel
# Last revision: 2018-05-16

active = 1

import numpy as np
import matplotlib.pyplot as plt
from random import *
from math import *
import csv

# Custom modules
from projections import *
from project import *
from constants import *
from utility import *

# Create utility object, calling correct financial data profile
# Currently available options: "so" and "scg"
ut = Utility("so", time_horizon, hist)

# Simulate plant construction project and return spend profiles
npp = Project()
npp.build_plant(active)

npp.get_lcoe(active)

print(npp.lcoe)

npp.get_npv(active)
print(npp.npv)

# Add CapEx to PPE
ut.ppe[:init_schedule] += npp.cum_spend
ut.ppe = prime_mover(ut.ppe, hist, ppe_growth)

# Add debt to debt
for i in range(npp.duration):
    ut.debt[i] += npp.cum_spend[i]/2

# Add interest to interest
for i in range(npp.duration):
    ut.interest[i] += npp.cum_spend[i]/2*mcd

#=====INCOME STATEMENT==================================================
#

ut.initialize_income_statement()

print(ut.net_income[:6])

#ut.revenues[hist:] += ann_rev

# Operating expenses
#ut.fuel[hist:] += ann_fuel
#ut.misc_om[hist:] += ann_om

#ut.capex[:init_schedule] += inc_spend
