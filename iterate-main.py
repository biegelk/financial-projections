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

num_iterations = 10000
make_plots = 1

npvs = np.zeros(num_iterations)
lcoes = np.zeros(num_iterations)
costs = np.zeros(num_iterations)
durations = np.zeros(num_iterations)
acps = np.zeros(num_iterations)

is_cash_shortage = np.zeros(num_iterations)
cash_shortage = np.zeros((num_iterations, time_horizon+hist))
no_problem = 0

for i in range(num_iterations):
    # Create utility object, calling selected financial data profile
    # Currently available options: "so" and "scg"
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    ut.initialize_CFS()

    # Simulate plant construction project and return spend profiles
    npp = Project()
    npp.build_plant()

    # Compute project LCOE
    npp.get_lcoe()
    if i == 495:
        print(npp.inc_idc)
        print(npp.inc_spend)
        print(npp.cum_spend)
        print("annual capital payment = $", npp.annual_capital_payment)

    # Compute project NPV
    npp.get_npv()

    ut.finance_project(npp)
    ut.incorporate_project(npp)

    ut.refresh_IS(hist)
    ut.refresh_CFS(npp, npp.duration)

    # Track outcomes
    costs[i] = npp.total_cost
    durations[i] = npp.duration
    npvs[i] = npp.npv
    lcoes[i] = npp.lcoe
    acps[i] = npp.annual_capital_payment

    if i == 495:
        ut.write_csv()

    for j in range(time_horizon + hist):
        if ut.fcf[j] <= 0.0:
            is_cash_shortage[i] += 1
            cash_shortage[i,j] = ut.fcf[j]

for j in range(num_iterations):
    if is_cash_shortage[j] == 0:
        no_problem += 1

print("average cost = ", np.mean(costs))
print("average duration = ", np.mean(durations))
print("stdev duration = ", np.std(durations))
print("average annual capital payment =", np.mean(acps))
#print("average npv = ", np.mean(npvs))
#print("average lcoe = ", np.mean(lcoes))
print("Average cash shortage years within forecast period = ", np.sum(is_cash_shortage) / num_iterations)
print("Std. dev cash shortage years w/in forecast period = ", np.std(is_cash_shortage))
print("Proportion of cases with no cash shortage = ", float(no_problem) / float(num_iterations))

total_cash_shortage = np.zeros(num_iterations)
for i in range(num_iterations):
    total_cash_shortage[i] = np.sum(cash_shortage[i,:])
print("Average total cash shortage within forecast period = ", np.mean(total_cash_shortage))
print("Std. dev total cash shortage within forecast period = ", np.std(total_cash_shortage))

with open('./results.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Cost', 'Duration', 'NPV', 'LCOE'])
    for i in range(num_iterations):
        writer.writerow([costs[i], durations[i], npvs[i], lcoes[i]])


# Generate plots
if make_plots:
    # Cost histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Total Construction Cost ($M)', title = 'Cost Outcomes')
    plt.hist(costs, 40)
    plt.show()

    # Duration histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Duration (years)', title = 'Project Duration Outcomes')
    plt.hist(durations, 40)
    plt.show()

    # LCOE histogram
#    fig = plt.figure()
#    ax = fig.add_subplot(111)
#    ax.set(xlabel = 'LCOE (cents/kWh)', title = 'Levelized Cost of Electricity Outcomes')
#    plt.hist(lcoes, 40)
#    plt.show()

    # NPV histogram
#    fig = plt.figure()
#    ax = fig.add_subplot(111)
#    ax.set(xlabel = 'NPV ($M)', title = 'Net Present Value Outcomes')
#    plt.hist(npvs, 40)
#    plt.show()

    # Annual capital payment histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Annual capital payment ($M)', title = 'Annual Capital Payment')
    plt.hist(acps, 40)
    plt.show()

    # Cash shortage histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Total Cash Shortage ($M)', title = 'Free Cash Flow Shortages')
    plt.hist(total_cash_shortage, 40)
    plt.show()


