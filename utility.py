import numpy as np
import csv

class Utility:
    """ Utility class represents financial records for a utility firm """

    def __init__(self, name, time_horizon, hist):
        """ Create a new utility instance """
        # Prime movers
        self.revenues = np.zeros(time_horizon+hist)
        self.fuel = np.zeros(time_horizon+hist)
        self.purchased_power = np.zeros(time_horizon+hist)
        self.depreciation = np.zeros(time_horizon+hist)
        self.ppe = np.zeros(time_horizon+hist)

        # Secondary movers
        self.misc_om = np.zeros(time_horizon+hist)
        self.misc_taxes = np.zeros(time_horizon+hist)
        self.tax_expense = np.zeros(time_horizon+hist)
        self.afudc = np.zeros(time_horizon+hist)
        self.misc_inc_exp = np.zeros(time_horizon+hist)
        self.income_tax = np.zeros(time_horizon+hist)
        self.interest = np.zeros(time_horizon+hist)
        self.debt = np.zeros(time_horizon+hist)
        self.capex = np.zeros(time_horizon+hist)

        # Summary lines
        self.gross_margin = np.zeros(time_horizon+hist)
        self.op_expenses = np.zeros(time_horizon+hist)
        self.ebitda = np.zeros(time_horizon+hist)
        self.op_expenses = np.zeros(time_horizon+hist)
        self.ebit = np.zeros(time_horizon+hist)
        self.ebt = np.zeros(time_horizon+hist)
        self.net_income = np.zeros(time_horizon+hist)
        self.fcf = np.zeros(time_horizon+hist)
        self.ebt = np.zeros(time_horizon+hist)
        self.delta_wc = np.zeros(time_horizon+hist)


        # Load financial data from csv
        if name == "so":
            datafile = "./profiles/income-statement-so.csv"
        elif name == "scg":
            datafile = "./profiles/income-statement-scg.csv"
        else:
            print("Utility not available")
            exit()
        with open(datafile, 'r') as df:
            fin_data = csv.reader(df, delimiter = ',', quotechar = '\"')
            for row in fin_data:
                self.revenues[0:hist]        = row[1:] if row[0] == 'TotalOperatingRevenues' else self.revenues[0:hist]
                self.fuel[0:hist]            = row[1:] if row[0] == 'Fuel'                   else self.fuel[0:hist]
                self.purchased_power[0:hist] = row[1:] if row[0] == 'PurchasedPower'         else self.purchased_power[0:hist]
                self.misc_om[0:hist]         = row[1:] if row[0] == 'OtherOM'                else self.misc_om[0:hist]
                self.depreciation[0:hist]    = row[1:] if row[0] == 'DepAmort'               else self.depreciation[0:hist]
                self.misc_taxes[0:hist]      = row[1:] if row[0] == 'NonIncomeTaxes'         else self.misc_taxes[0:hist]
                self.afudc[0:hist]           = row[1:] if row[0] == 'AFUDC'                  else self.afudc[0:hist]
                self.interest[0:hist]        = row[1:] if row[0] == 'InterestExpense'        else self.interest[0:hist]
                self.income_tax[0:hist]      = row[1:] if row[0] == 'IncomeTaxes'            else self.income_tax[0:hist]
                self.debt[0:hist]            = row[1:] if row[0] == 'LTD'                    else self.debt[0:hist]
                self.ppe[0:hist]             = row[1:] if row[0] == 'TotalPPE'               else self.ppe[0:hist]
                self.capex[0:hist]           = row[1:] if row[0] == 'CapEx'                  else self.capex[0:hist]
                self.delta_wc[0:hist]        = row[1:] if row[0] == 'DeltaWC'                else self.delta_wc[0:hist]

