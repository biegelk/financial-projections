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

num_iterations = 100000
make_plots = 1

npvs = np.zeros(num_iterations)
lcoes = np.zeros(num_iterations)
costs = np.zeros(num_iterations)
durations = np.zeros(num_iterations)
acps = np.zeros(num_iterations)
cidcs = np.zeros((num_iterations, 16))

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
    npp.build_plant(ut)

    # Compute project LCOE
    npp.get_lcoe()
    if i == 495:
        print(npp.inc_idc)
        print(npp.cum_idc)
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
    for j in range(int(m.ceil(npp.duration))):
        if npp.cum_idc[j] != 0:
            cidcs[i,j] = npp.cum_idc[j]

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

# Trim IDC outputs
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(num_iterations):
    for j in range(5, 16):
        if cidcs[i, j] != 0:
            counts[j-5] += 1

trim_cidc5 = np.zeros(counts[0])
trim_cidc6 = np.zeros(counts[1])
trim_cidc7 = np.zeros(counts[2])
trim_cidc8 = np.zeros(counts[3])
trim_cidc9 = np.zeros(counts[4])
trim_cidc10 = np.zeros(counts[5])
trim_cidc11 = np.zeros(counts[6])
trim_cidc12 = np.zeros(counts[7])
trim_cidc13 = np.zeros(counts[8])
trim_cidc14 = np.zeros(counts[9])
trim_cidc15 = np.zeros(counts[10])

j1 = 0
j2 = 0
j3 = 0
j4 = 0
j5 = 0
j6 = 0
j7 = 0
j8 = 0
j9 = 0
j10 = 0
j11 = 0

for i in range(num_iterations):
    if cidcs[i, 5] != 0:
        trim_cidc5[j1] = cidcs[i, 5]
        j1 += 1
    if cidcs[i, 6] != 0:
        trim_cidc6[j2] = cidcs[i, 6]
        j2 += 1
    if cidcs[i, 7] != 0:
        trim_cidc7[j3] = cidcs[i, 7]
        j3 += 1
    if cidcs[i, 8] != 0:
        trim_cidc8[j4] = cidcs[i, 8]
        j4 += 1
    if cidcs[i, 9] != 0:
        trim_cidc9[j5] = cidcs[i, 9]
        j5 += 1
    if cidcs[i, 10] != 0:
        trim_cidc10[j6] = cidcs[i, 10]
        j6 += 1
    if cidcs[i, 11] != 0:
        trim_cidc11[j7] = cidcs[i, 11]
        j7 += 1
    if cidcs[i, 12] != 0:
        trim_cidc12[j8] = cidcs[i, 12]
        j8 += 1
    if cidcs[i, 13] != 0:
        trim_cidc13[j9] = cidcs[i, 13]
        j9 += 1
    if cidcs[i, 14] != 0:
        trim_cidc14[j10] = cidcs[i, 14]
        j10 += 1
    if cidcs[i, 15] != 0:
        trim_cidc15[j11] = cidcs[i, 15]
        j11 += 1

with open('./data/results.csv', 'w') as outfile:
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
    plt.hist(costs, int(num_iterations / 50.))
    plt.show()

    # Duration histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Duration (years)', title = 'Project Duration Outcomes')
    plt.hist(durations, 40)
    plt.show()

#    for j in range(15):
#        fig = plt.figure()
#        ax = fig.add_subplot(111)
#        ax.set(xlabel = 'Cumulative IDC' + str(j), title = 'IDC over time')
#        plt.hist(cidcs[:,j], 1000)
#        plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 5', title = 'Interest During Construction')
    plt.hist(trim_cidc5, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 6', title = 'Interest During Construction')
    plt.hist(trim_cidc6, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 7', title = 'Interest During Construction')
    plt.hist(trim_cidc7, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 8', title = 'Interest During Construction')
    plt.hist(trim_cidc8, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 9', title = 'Interest During Construction')
    plt.hist(trim_cidc9, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 10', title = 'Interest During Construction')
    plt.hist(trim_cidc10, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 11', title = 'Interest During Construction')
    plt.hist(trim_cidc11, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 12', title = 'Interest During Construction')
    plt.hist(trim_cidc12, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 13', title = 'Interest During Construction')
    plt.hist(trim_cidc13, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 14', title = 'Interest During Construction')
    plt.hist(trim_cidc14, 1000)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlabel = 'Cumulative IDC 15', title = 'Interest During Construction')
    plt.hist(trim_cidc15, 1000)
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


