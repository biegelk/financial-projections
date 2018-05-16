# A pro forma financial statement generator for SO-type firms.
# Author: Katie Biegel
# Last revision: 2018-05-16
# Last revision: loading data from csv, modularization
# note: fix ebt off-by-one error in 2016 and 2017

import numpy as np
import matplotlib.pyplot as plt
from random import *
from math import *
import csv

# Custom modules
from projections import *
from build import *

#################################
# CONSTANTS
#################################

# Define time horizon for projections (years)
time_horizon = 10
current_year = 2018
hist = 6

# Firm financial constants
tax_rate = 0.335
wacd = 0.05 # historical weighted average cost of debt
mcd = 0.07  # marginal cost of debt for a nuclear project

## Project constants
total_cost = 4000 # $M, cost estimate at 0% completion
init_schedule = 5 # construction schedule, years
capacity = 2200000 # kW
cf = 0.9 # capacity factor
d = (9.25+4.)/2./100. # wacc/discount rate
term = 30 # years
power_price = 0.06 # $/kWh
life = 40 # years

# Cost escalation parameters
# Completion milestones
completion_steps = [0, .25, .5, .75, .9, 1]
# Gamma-distribution parameters of empirical escalation data
cgamma_params = [[1.236, 1/2.942], [19.893, 1/21.711], [50.734, 1/24.857], [17.499, 1/17.438]]
cgamma_fix = [0, .73, 1.54, 0.90, 0]

# Growth rates
rev_growth  = 0.016  # % change YOY
fuel_growth = 0.252  # % of revenues
pp_growth   = 0.042  # % of revenues
ppe_growth  = 0.03   # % change YOY

# Secondary ratios
misc_om_ratio = 0.256  # to revenues
fuel_ratio    = 0.252  # to revenues
pp_ratio      = 0.042  # to revenues
misc_taxes_ratio = 0.128 # to EBITDA


###################################################################
# FINANCIAL STATEMENT GENERATOR
###################################################################


# Declare arrays for prime movers
revenues = np.zeros(time_horizon+hist)
fuel = np.zeros(time_horizon+hist)
purchased_power = np.zeros(time_horizon+hist)
depreciation = np.zeros(time_horizon+hist)
ppe = np.zeros(time_horizon+hist)

# Declare arrays for secondary movers
misc_om = np.zeros(time_horizon+hist)
misc_taxes = np.zeros(time_horizon+hist)
tax_expense = np.zeros(time_horizon+hist)
afudc = np.zeros(time_horizon+hist)
misc_inc_exp = np.zeros(time_horizon+hist)
income_tax = np.zeros(time_horizon+hist)
interest = np.zeros(time_horizon+hist)
debt = np.zeros(time_horizon+hist)
capex = np.zeros(time_horizon+hist)

# Declare arrays for summary lines
gross_margin = np.zeros(time_horizon+hist)
op_expenses = np.zeros(time_horizon+hist)
ebitda = np.zeros(time_horizon+hist)
op_expenses = np.zeros(time_horizon+hist)
ebit = np.zeros(time_horizon+hist)
ebt = np.zeros(time_horizon+hist)
net_income = np.zeros(time_horizon+hist)
fcf = np.zeros(time_horizon+hist)
ebt = np.zeros(time_horizon+hist)
delta_wc = np.zeros(time_horizon+hist)


# Load financial data from csv (adapted from SO, 2012-2017)
with open('./profiles/income-statement-so.csv', 'r') as df:
    fin_data = csv.reader(df, delimiter = ',', quotechar = '\"')
    for row in fin_data:
        hist = len(row)-1
        revenues[0:hist] = row[1:] if row[0] == 'TotalOperatingRevenues' else revenues[0:hist]
        fuel[0:hist]            = row[1:] if row[0] == 'Fuel'                   else fuel[0:hist]
        purchased_power[0:hist] = row[1:] if row[0] == 'PurchasedPower'         else purchased_power[0:hist]
        misc_om[0:hist]         = row[1:] if row[0] == 'OtherOM'                else misc_om[0:hist]
        depreciation[0:hist]    = row[1:] if row[0] == 'DepAmort'               else depreciation[0:hist]
        misc_taxes[0:hist]      = row[1:] if row[0] == 'NonIncomeTaxes'         else misc_taxes[0:hist]
        afudc[0:hist]           = row[1:] if row[0] == 'AFUDC'                  else afudc[0:hist]
        interest[0:hist]        = row[1:] if row[0] == 'InterestExpense'        else interest[0:hist]
        income_tax[0:hist]      = row[1:] if row[0] == 'IncomeTaxes'            else income_tax[0:hist]
        debt[0:hist]            = row[1:] if row[0] == 'LTD'                    else debt[0:hist]
        ppe[0:hist]             = row[1:] if row[0] == 'TotalPPE'               else ppe[0:hist]
        capex[0:hist]           = row[1:] if row[0] == 'CapEx'                  else capex[0:hist]
        delta_wc[0:hist]        = row[1:] if row[0] == 'DeltaWC'                else delta_wc[0:hist]
 
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
lcoe = (ann_cap_cost + ann_fuel + ann_om) / ann_gen

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
ppe[:init_schedule] += cum_spend
ppe = prime_mover(ppe, hist, ppe_growth)

# Add debt to debt
for i in range(init_schedule):
    debt[i] += cum_spend[i]/2

# Add interest to interest
for i in range(init_schedule):
    interest[i] += cum_spend[i]/2*mcd

#=====INCOME STATEMENT==================================================
#
# Operating revenues
revenues = prime_mover(revenues, hist, rev_growth)
revenues[hist:] += ann_rev

# Operating expenses
fuel = secondary_mover(fuel, revenues, hist, fuel_ratio)
fuel[hist:] += ann_fuel
purchased_power = secondary_mover(purchased_power, revenues, hist, pp_ratio)
misc_om = secondary_mover(misc_om, revenues, hist, misc_om_ratio)
misc_om[hist:] += ann_om
op_expenses = summary_line(op_expenses, fuel, purchased_power, misc_om)

# EBITDA
ebitda = summary_line(ebitda, revenues, op_expenses*(-1))

# Other expenses
depreciation = prime_mover(depreciation, hist, 0.0)
misc_taxes = secondary_mover(misc_taxes, ebitda, hist, misc_taxes_ratio)

# EBIT
ebit = summary_line(ebit, ebitda, (-1)*depreciation, (-1)*misc_taxes)

# Post-EBIT expenses
afudc = prime_mover(afudc, hist, 0.0)
interest = secondary_mover(interest, debt, hist, wacd)

# EBT
ebt = summary_line(ebt, ebit, afudc, (-1)*interest)

# Income taxes
income_tax = secondary_mover(income_tax, ebt, hist, tax_rate)

# Net income
net_income = summary_line(net_income, ebt, (-1)*income_tax)

print(net_income)

capex = secondary_mover(capex, revenues, hist, ppe_growth)
capex[:init_schedule] += inc_spend

print(capex)

delta_wc = prime_mover(delta_wc, hist, 0.0)

fcf = net_income + depreciation - capex - delta_wc

print(fcf)

################################




##############################################################################################################################
# PLOTS

#x = np.arange(14)
#years = np.arange(current_year-4,current_year-4+time_horizon)

#plt.plot(x,revenues)
#plt.xlabel(years)
#plt.show()
