import numpy as np
import csv
from projections import *
from constants import *

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
        self.afudc = np.zeros(time_horizon+hist)
        self.income_tax = np.zeros(time_horizon+hist)
        self.interest = np.zeros(time_horizon+hist)
        self.debt = np.zeros(time_horizon+hist)
        self.capex = np.zeros(time_horizon+hist)

        # Summary lines
        self.op_expenses = np.zeros(time_horizon+hist)
        self.ebitda = np.zeros(time_horizon+hist)
        self.ebit = np.zeros(time_horizon+hist)
        self.ebt = np.zeros(time_horizon+hist)
        self.net_income = np.zeros(time_horizon+hist)
        self.fcf = np.zeros(time_horizon+hist)
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


    def initialize_IS(self):
        # Operating revenues
        self.revenues = prime_mover(self.revenues, hist, rev_growth)

        # Operating expenses
        self.fuel = secondary_mover(self.fuel, self.revenues, hist, fuel_ratio)
        self.purchased_power = secondary_mover(self.purchased_power, self.revenues, hist, pp_ratio)
        self.misc_om = secondary_mover(self.misc_om, self.revenues, hist, misc_om_ratio)
        self.op_expenses = summary_line(self.op_expenses, self.fuel, self.purchased_power, self.misc_om)

        # EBITDA
        self.ebitda = summary_line(self.ebitda, self.revenues, self.op_expenses*(-1))

        # Other expenses
        self.depreciation = prime_mover(self.depreciation, hist, 0.0)
        self.misc_taxes = secondary_mover(self.misc_taxes, self.ebitda, hist, misc_taxes_ratio)

        # EBIT
        self.ebit = summary_line(self.ebit, self.ebitda, (-1)*self.depreciation, (-1)*self.misc_taxes)

        # Post-EBIT expenses
        self.afudc = prime_mover(self.afudc, hist, 0.0)
        self.interest = secondary_mover(self.interest, self.debt, hist, wacd)

        # EBT
        self.ebt = summary_line(self.ebt, self.ebit, self.afudc, (-1)*self.interest)

        # Income taxes
        self.income_tax = secondary_mover(self.income_tax, self.ebt, hist, tax_rate)

        # Net income
        self.net_income = summary_line(self.net_income, self.ebt, (-1)*self.income_tax)

        # Capital Expenditures
        self.capex = secondary_mover(self.capex, self.revenues, hist, ppe_growth)

        # Debt
        self.debt = prime_mover(self.debt, hist, 0.0)

        # Change in Working Capital
        self.delta_wc = prime_mover(self.delta_wc, hist, 0.0)

        # Free Cash Flow
        self.fcf = self.net_income + self.depreciation - self.capex - self.delta_wc



    def refresh_IS(self):
        self.misc_om = secondary_mover(self.misc_om, self.revenues, hist, misc_om_ratio)
        self.misc_taxes = secondary_mover(self.misc_taxes, self.ebitda, hist, misc_taxes_ratio)
        self.op_expenses = summary_line(self.op_expenses, self.fuel, self.purchased_power, self.misc_om)
        self.ebitda = summary_line(self.ebitda, self.revenues, self.op_expenses*(-1))
        self.misc_taxes = secondary_mover(self.misc_taxes, self.ebitda, hist, misc_taxes_ratio)
        self.ebit = summary_line(self.ebit, self.ebitda, (-1)*self.depreciation, (-1)*self.misc_taxes)
        self.interest = secondary_mover(self.interest, self.debt, hist, wacd)
        self.ebt = summary_line(self.ebt, self.ebit, self.afudc, (-1)*self.interest)
        self.income_tax = secondary_mover(self.income_tax, self.ebt, hist, tax_rate)
        self.net_income = summary_line(self.net_income, self.ebt, (-1)*self.income_tax)
        self.capex = secondary_mover(self.capex, self.revenues, hist, ppe_growth)
        self.fcf = summary_line(self.net_income, self.depreciation, (-1)*self.capex, (-1)*self.delta_wc)


    def write_IS_csv(self):
        with open('checkfile.csv', 'w') as checkfile:
            writer = csv.writer(checkfile, delimiter = ',', quotechar = '\"')
            writer.writerow(['', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027'])
            writer.writerow(np.concatenate((['Revenues'],self.revenues)))
            writer.writerow(np.concatenate((['Fuel'], self.fuel)))
            writer.writerow(np.concatenate((['Purchased Power'], self.purchased_power)))
            writer.writerow(np.concatenate((['Misc OM'], self.misc_om)))
            writer.writerow(np.concatenate((['Operating Expenses'], self.op_expenses)))
            writer.writerow(np.concatenate((['EBITDA'], self.ebitda)))
            writer.writerow(np.concatenate((['Depreciation'], self.depreciation)))
            writer.writerow(np.concatenate((['Non-Income Taxes'], self.misc_taxes)))
            writer.writerow(np.concatenate((['EBIT'], self.ebit)))
            writer.writerow(np.concatenate((['AFUDC'], self.afudc)))
            writer.writerow(np.concatenate((['Interest Expense'], self.interest)))
            writer.writerow(np.concatenate((['EBT'], self.ebt)))
            writer.writerow(np.concatenate((['Income Tax'], self.income_tax)))
            writer.writerow(np.concatenate((['Net Income'], self.net_income)))
            writer.writerow('\n')
            writer.writerow(np.concatenate((['Total Debt'], self.debt)))
