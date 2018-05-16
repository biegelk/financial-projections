# Testing pulling data from csv
# 16 May 2018

stuff = [0, 0, 0, 0, 0, 0]
junk = [0, 0, 0, 0, 0, 0]

import csv
with open('income-statement.csv', 'r') as df:
    fin_data = csv.reader(df, delimiter = ',', quotechar = '\"')
    for row in fin_data:
        stuff[1] = row[1] if row[0] == 'Fuel' else stuff[1]
        junk[1] = row[1] if row[0] == 'TotalPPE' else junk[1]
print(stuff)
print(junk)
