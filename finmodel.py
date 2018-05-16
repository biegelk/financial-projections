# A pro forma financial statement generator for a utility building
#     a nuclear power plant.
# Author: Katie Biegel
# Last revision: 2018-05-16
# note: fix ebt off-by-one error in 2016 and 2017

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

ut = Utility("so", time_horizon, hist)

(inc_spend, cum_spend) = build_plant(total_cost, init_schedule)

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
# Operating revenues
ut.revenues = prime_mover(ut.revenues, hist, rev_growth)
ut.revenues[hist:] += ann_rev

# Operating expenses
ut.fuel = secondary_mover(ut.fuel, ut.revenues, hist, fuel_ratio)
ut.fuel[hist:] += ann_fuel
ut.purchased_power = secondary_mover(ut.purchased_power, ut.revenues, hist, pp_ratio)
ut.misc_om = secondary_mover(ut.misc_om, ut.revenues, hist, misc_om_ratio)
ut.misc_om[hist:] += ann_om
ut.op_expenses = summary_line(ut.op_expenses, ut.fuel, ut.purchased_power, ut.misc_om)

# EBITDA
ut.ebitda = summary_line(ut.ebitda, ut.revenues, ut.op_expenses*(-1))

# Other expenses
ut.depreciation = prime_mover(ut.depreciation, hist, 0.0)
ut.misc_taxes = secondary_mover(ut.misc_taxes, ut.ebitda, hist, misc_taxes_ratio)

# EBIT
ut.ebit = summary_line(ut.ebit, ut.ebitda, (-1)*ut.depreciation, (-1)*ut.misc_taxes)

# Post-EBIT expenses
ut.afudc = prime_mover(ut.afudc, hist, 0.0)
ut.interest = secondary_mover(ut.interest, ut.debt, hist, wacd)

# EBT
ut.ebt = summary_line(ut.ebt, ut.ebit, ut.afudc, (-1)*ut.interest)

# Income taxes
ut.income_tax = secondary_mover(ut.income_tax, ut.ebt, hist, tax_rate)

# Net income
ut.net_income = summary_line(ut.net_income, ut.ebt, (-1)*ut.income_tax)

print(ut.net_income)

ut.capex = secondary_mover(ut.capex, ut.revenues, hist, ppe_growth)
ut.capex[:init_schedule] += inc_spend

print(ut.capex)

ut.delta_wc = prime_mover(ut.delta_wc, hist, 0.0)

ut.fcf = ut.net_income + ut.depreciation - ut.capex - ut.delta_wc

print(ut.fcf)

################################

# PLOTS

#x = np.arange(14)
#years = np.arange(current_year-4,current_year-4+time_horizon)

#plt.plot(x,revenues)
#plt.xlabel(years)
#plt.show()
