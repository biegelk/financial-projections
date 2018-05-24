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

# Add CapEx to PPE
ut.ppe[:m.ceil(npp.duration)] += npp.cum_spend
ut.ppe = prime_mover(ut.ppe, hist, ppe_growth)

# Account for plant capital cost effects
for i in range(m.ceil(npp.duration)-1):
    ut.debt[i] += npp.cum_spend[i]/2

# Account for plant operational outcomes
ut.revenues[m.ceil(npp.duration)-1:] += npp.annual_revenue
ut.fuel[m.ceil(npp.duration)-1:] += npp.annual_fuel_cost
ut.misc_om[m.ceil(npp.duration)-1:] += npp.annual_om_cost


ut.refresh_IS(hist)

#ut.capex[:init_schedule] += inc_spend

ut.write_IS_csv()
