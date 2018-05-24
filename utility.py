import numpy as np
import csv
import math as m
from projections import *
from constants import *

class Utility:
    """ Utility class represents financial records for a utility firm """

    def __init__(self, name, time_horizon, hist):
        """ Create a new utility instance """

        ## INCOME STATEMENT

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
        self.npp_interest = np.zeros(time_horizon+hist)
        self.baseline_interest = np.zeros(time_horizon+hist)
        self.debt = np.zeros(time_horizon+hist)
        self.capex = np.zeros(time_horizon+hist)

        # Summary lines
        self.op_expenses = np.zeros(time_horizon+hist)
        self.ebitda = np.zeros(time_horizon+hist)
        self.ebit = np.zeros(time_horizon+hist)
        self.interest = np.zeros(time_horizon+hist)
        self.ebt = np.zeros(time_horizon+hist)
        self.net_income = np.zeros(time_horizon+hist)


        ## BALANCE SHEET
        self.npp_debt = np.zeros(time_horizon+hist)
        self.baseline_debt = np.zeros(time_horizon+hist)
        self.total_debt = np.zeros(time_horizon+hist)


        ## CASH FLOW STATEMENT
        self.dividends = np.zeros(time_horizon+hist)
        self.baseline_delta_wc = np.zeros(time_horizon+hist)
        self.delta_wc = np.zeros(time_horizon+hist)
        self.fcf = np.zeros(time_horizon+hist)
        self.shares_outstanding = np.zeros(time_horizon+hist)
        self.dps = np.zeros(time_horizon+hist)




        # Capital Structure
        self.debt_fraction = 0.5
        self.equity_fraction = 1 - self.debt_fraction


        # Load financial data from csv
        if name == "so":
            isfile = "./profiles/income-statement-so.csv"
        elif name == "scg":
            isfile = "./profiles/income-statement-scg.csv"
        else:
            print("Utility IS not available")
            exit()
        with open(isfile, 'r') as df:
            is_data = csv.reader(df, delimiter = ',', quotechar = '\"')
            for row in is_data:
                self.revenues[0:hist]        = row[1:] if row[0] == 'TotalOperatingRevenues' else self.revenues[0:hist]
                self.fuel[0:hist]            = row[1:] if row[0] == 'Fuel'                   else self.fuel[0:hist]
                self.purchased_power[0:hist] = row[1:] if row[0] == 'PurchasedPower'         else self.purchased_power[0:hist]
                self.misc_om[0:hist]         = row[1:] if row[0] == 'OtherOM'                else self.misc_om[0:hist]
                self.depreciation[0:hist]    = row[1:] if row[0] == 'DepAmort'               else self.depreciation[0:hist]
                self.misc_taxes[0:hist]      = row[1:] if row[0] == 'NonIncomeTaxes'         else self.misc_taxes[0:hist]
                self.afudc[0:hist]           = row[1:] if row[0] == 'AFUDC'                  else self.afudc[0:hist]
                self.baseline_interest[0:hist] = row[1:] if row[0] == 'InterestExpense'      else self.baseline_interest[0:hist]
                self.income_tax[0:hist]      = row[1:] if row[0] == 'IncomeTaxes'            else self.income_tax[0:hist]
                self.baseline_debt[0:hist]   = row[1:] if row[0] == 'LTD'                    else self.baseline_debt[0:hist]
                self.ppe[0:hist]             = row[1:] if row[0] == 'TotalPPE'               else self.ppe[0:hist]
                self.capex[0:hist]           = row[1:] if row[0] == 'CapEx'                  else self.capex[0:hist]
                self.delta_wc[0:hist]        = row[1:] if row[0] == 'DeltaWC'                else self.delta_wc[0:hist]
        if name == "so":
            cfsfile = "./profiles/cash-flow-statement-so.csv"
        else:
            print("Utility CFS not available")
        with open(cfsfile, 'r') as df:
            cfs_data = csv.reader(df, delimiter = ',', quotechar = '\"')
            for row in cfs_data:
                self.dividends[0:hist] = row[1:] if row[0] == 'Dividends' else self.dividends[0:hist]
                self.shares_outstanding[0:hist] = row[1:] if row[0] == 'SharesOutstanding' else self.shares_outstanding[0:hist]
                self.capex[0:hist] = row[1:] if row[0] == 'CapEx' else self.capex[0:hist]
                self.delta_wc[0:hist] = row[1:] if row[0] == 'DeltaWC' else self.delta_wc[0:hist]



    def initialize_IS(self):
        # Debt
        self.baseline_debt = prime_mover(self.baseline_debt, hist, 0.0)
        self.total_debt = summary_line(self.total_debt, self.baseline_debt, self.npp_debt)

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
        self.baseline_interest = secondary_mover(self.baseline_interest, self.baseline_debt, hist, wacd)
        self.npp_interest = secondary_mover(self.npp_interest, self.npp_debt, hist, mcd)
        self.interest = summary_line(self.interest, self.baseline_interest, self.npp_interest)

        # EBT
        self.ebt = summary_line(self.ebt, self.ebit, self.afudc, (-1)*self.interest)

        # Income taxes
        self.income_tax = secondary_mover(self.income_tax, self.ebt, hist, tax_rate)

        # Net income
        self.net_income = summary_line(self.net_income, self.ebt, (-1)*self.income_tax)



    def refresh_IS(self, hist):
        self.total_debt = summary_line(self.total_debt, self.baseline_debt, self.npp_debt)
        self.misc_om = secondary_mover(self.misc_om, self.revenues, hist, misc_om_ratio)
        self.misc_taxes = secondary_mover(self.misc_taxes, self.ebitda, hist, misc_taxes_ratio)
        self.op_expenses = summary_line(self.op_expenses, self.fuel, self.purchased_power, self.misc_om)
        self.ebitda = summary_line(self.ebitda, self.revenues, self.op_expenses*(-1))
        self.misc_taxes = secondary_mover(self.misc_taxes, self.ebitda, hist, misc_taxes_ratio)
        self.ebit = summary_line(self.ebit, self.ebitda, (-1)*self.depreciation, (-1)*self.misc_taxes)
        self.baseline_interest = secondary_mover(self.baseline_interest, self.baseline_debt, 0, wacd)
        self.npp_interest = secondary_mover(self.npp_interest, self.npp_debt, 0, mcd)
        self.interest = summary_line(self.interest, self.baseline_interest, self.npp_interest)
        self.ebt = summary_line(self.ebt, self.ebit, self.afudc, (-1)*self.interest)
        self.income_tax = secondary_mover(self.income_tax, self.ebt, hist, tax_rate)
        self.net_income = summary_line(self.net_income, self.ebt, (-1)*self.income_tax)

    def write_csv(self):
        with open('checkfile.csv', 'w') as checkfile:
            writer = csv.writer(checkfile, delimiter = ',', quotechar = '\"')
            # Income Statement
            writer.writerow(['', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027'])
            writer.writerow(['INCOME STATEMENT'])
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
            # Balance Sheet
            writer.writerow(['', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027'])
            writer.writerow(['BALANCE SHEET'])
            writer.writerow(np.concatenate((['Baseline Debt'], self.baseline_debt)))
            writer.writerow(np.concatenate((['Project Debt'], self.npp_debt)))
            writer.writerow(np.concatenate((['Total Debt'], self.total_debt)))
            writer.writerow('\n')
            # Cash Flow Statement
            writer.writerow(['', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027'])
            writer.writerow(np.concatenate((['Delta Working Capital'], self.delta_wc)))
            writer.writerow(np.concatenate((['CapEx'], self.capex)))
            writer.writerow(np.concatenate((['Free Cash Flow'], self.fcf)))
            writer.writerow(np.concatenate((['Dividends Paid'], self.dividends)))
            writer.writerow(np.concatenate((['Shares Outstanding'], self.shares_outstanding)))
            writer.writerow(np.concatenate((['Dividend Yield'], self.dps)))


    def incorporate_project(self, npp):
        # Add NPP spend to PPE
        self.ppe[:m.ceil(npp.duration)] += npp.cum_spend
        self.ppe = prime_mover(self.ppe, m.ceil(npp.duration), ppe_growth)

        # Add NPP spend to CapEx and Change in Working Capital
        self.capex[:m.ceil(npp.duration)] += npp.inc_spend
#        self.delta_wc[:m.ceil(npp.duration)] -= 2400
        ### SKETCHY--FIX
        self.delta_wc -= 2400

        # Straight-line depreciation once project is complete
        for i in range(m.ceil(npp.duration),time_horizon+hist):
            self.depreciation[i:] += npp.total_cost / econ_life

        # Account for project-related debt
        self.npp_debt[:m.ceil(npp.duration)] = npp.cum_spend * self.debt_fraction
        self.npp_debt = prime_mover(self.npp_debt, m.ceil(npp.duration), 0.0)

        # Account for plant operational outcomes
        self.revenues[m.ceil(npp.duration)-1:] += npp.annual_revenue
        self.fuel[m.ceil(npp.duration)-1:] += npp.annual_fuel_cost
        self.misc_om[m.ceil(npp.duration)-1:] += npp.annual_om_cost


    def initialize_CFS(self):
        # Dividends
        self.dividends = prime_mover(self.dividends, hist, dps_growth)

        # Capital Expenditures
        self.capex = prime_mover(self.capex, hist, ppe_growth)

        # Change in Working Capital
        self.baseline_delta_wc = prime_mover(self.delta_wc, hist, 0.0)
        self.delta_wc = summary_line(self.delta_wc, self.baseline_delta_wc)

        # Free Cash Flow
        self.fcf = summary_line(self.fcf, self.net_income, self.depreciation, (-1)*self.capex, (-1)*self.delta_wc)

        # Shares outstanding
        self.shares_outstanding = prime_mover(self.shares_outstanding, hist, 0.0)
        self.dps = metric_ratio(self.dps, self.dividends, self.shares_outstanding)

       
    def refresh_CFS(self, npp, hist):
        self.capex = prime_mover(self.capex, m.ceil(hist), 0.0)
        self.fcf = summary_line(self.fcf, self.net_income, self.depreciation, (-1)*self.capex, (-1)*self.delta_wc)
        self.shares_outstanding = prime_mover(self.shares_outstanding, m.ceil(npp.duration), 0.0)
        self.dps = metric_ratio(self.dps, self.dividends, self.shares_outstanding)      

