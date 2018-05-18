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
from build import *
from constants import *
from utility import *

# Create utility object, calling selected financial data profile
# Currently available options: "so" and "scg"
ut = Utility("so", time_horizon, hist)
ut.initialize_IS()

# Simulate plant construction project and return spend profiles
npp = Project()
npp.build_plant(active)

# Compute project LCOE
npp.get_lcoe(active)
print("LCOE = ",npp.lcoe,"c/kWh")

# Compute project NPV
npp.get_npv(active)
print("NPV = $", npp.npv,"M")

# Add CapEx to PPE
ut.ppe[:init_schedule] += npp.cum_spend
ut.ppe = prime_mover(ut.ppe, hist, ppe_growth)

# Account for plant capital cost effects
for i in range(npp.duration):
    ut.debt[i] += npp.cum_spend[i]/2

# Account for plant operational outcomes
if active:
    ut.revenues[npp.duration:] += npp.annual_revenue
    ut.fuel[npp.duration:] += npp.annual_fuel_cost
    ut.misc_om[npp.duration:] += npp.annual_om_cost
else:
    pass

print(ut.debt)

ut.refresh_IS()

print(ut.debt)

#ut.capex[:init_schedule] += inc_spend
