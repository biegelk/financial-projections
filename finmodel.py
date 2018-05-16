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

# Create utility object, calling correct financial data profile
# Currently available options: "so" and "scg"
ut = Utility("so", time_horizon, hist)

# Simulate plant construction project and return spend profiles
(inc_spend, cum_spend) = build_plant(0, init_schedule)

## GENERATION COST AND REVENUE PROFILE
# Annual electricity generated
ann_gen = capacity * cf * 8766 # kWh/yr

# Annual cost sources
ann_fuel = 151
ann_om = 139

# Annual revenues from electricity sales
ann_rev = power_price * ann_gen / 1e6

## LCOE
# Calculate levelized cost of electricity needed to justify investment
#lcoe = (ann_cap_cost + ann_fuel + ann_om) / ann_gen

## NET PRESENT VALUE
# Initialize variables
#cap_npv = 0
#rev_npv = 0
#fuel_npv = 0
#om_npv = 0

# Calculate sinking fund factor for total incurred construction costs
#cap_payment = total_cost * d / (1-(1+d)**(-term))

# Annual costs during debt-repayment period
#for i in range(term):
#    cap_npv += cap_payment / (1+d)**(i)
#    rev_npv += ann_rev / (1+d)**(i)
#    fuel_npv += ann_fuel / (1+d-.02)**(i)
#    om_npv += ann_om / (1+d-.02)**(i)

# Annual costs after debt is repaid
#for i in range(term, life):
#    rev_npv += ann_rev / (1+d)**(i)
#    fuel_npv += ann_fuel / (1+d-.02)**(i)
#    om_npv += ann_om / (1+d-.02)**(i)

# Resultant NPV
#npv = rev_npv - cap_npv - fuel_npv - om_npv

# Add CapEx to PPE
ut.ppe[:init_schedule] += cum_spend
ut.ppe = prime_mover(ut.ppe, hist, ppe_growth)

# Add debt to debt
for i in range(init_schedule):
    ut.debt[i] += cum_spend[i]/2

# Add interest to interest
for i in range(init_schedule):
    ut.interest[i] += cum_spend[i]/2*mcd

#=====INCOME STATEMENT==================================================
#

ut.initialize_income_statement()

#ut.revenues[hist:] += ann_rev

# Operating expenses
#ut.fuel[hist:] += ann_fuel
#ut.misc_om[hist:] += ann_om

#ut.capex[:init_schedule] += inc_spend


################################

# PLOTS

#x = np.arange(14)
#years = np.arange(current_year-4,current_year-4+time_horizon)

#plt.plot(x,revenues)
#plt.xlabel(years)
#plt.show()
