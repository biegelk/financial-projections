from projections import *
from build import *
from utility import *
from constants import *

import numpy as np
import random as rand
from math import *
import csv

## TEST NONSUMMARY IMPORTATION

def test_import_IS_revenues():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.revenues[hist-1])) == 15000

def test_import_IS_fuel():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.fuel[hist-1])) == 3780

def test_import_IS_purchased_power():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.purchased_power[hist-1])) == 630

def test_import_IS_misc_om():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.misc_om[hist-1])) == 3840

def test_import_IS_depreciation():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.depreciation[hist-1])) == 2000

def test_import_IS_misc_taxes():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.misc_taxes[hist-1])) == 864

def test_import_IS_afudc():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.afudc[hist-1])) == 200

def test_import_IS_baseline_interest():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.baseline_interest[hist-1])) == 1000

def test_import_IS_income_tax():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.income_tax[hist-1])) == 1034

def test_import_IS_baseline_debt():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.baseline_debt[hist-1])) == 20000

def test_import_CFS_capex():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.capex[hist-1])) == 4000

def test_import_CFS_shares_outstanding():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.shares_outstanding[hist-1])) == 1000

def test_import_CFS_dividends_paid():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.dividends_paid[hist-1])) == 1026

def test_import_CFS_share_price():
    ut = Utility("check", time_horizon, hist)
    assert int(round(ut.share_price[hist-1])) == 30


## TEST INITIAL (PRE-PROJECT) INCOME STATEMENT REFRESH

def test_initialize_IS_baseline_debt():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.baseline_debt[hist-1])) == 20000
    assert int(round(ut.baseline_debt[-1])) == 20000

def test_initialize_IS_total_debt():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.total_debt[hist-1])) == 20000
    assert int(round(ut.total_debt[-1])) == 20000

def test_initialize_IS_revenue():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.revenues[-1])) == 17580

def test_initialize_IS_fuel():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.fuel[-1])) == 4430

def test_initialize_IS_purchased_power():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.purchased_power[-1])) == 738

def test_initialize_IS_misc_om():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.misc_om[-1])) == 4501

def test_initialize_IS_op_expenses():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.op_expenses[hist-1])) == 8250
    assert int(round(ut.op_expenses[-1])) == 9669

def test_initialize_IS_ebitda():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.ebitda[hist-1])) == 6750
    assert int(round(ut.ebitda[-1])) == 7911

def test_initialize_IS_depreciation():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.depreciation[-1])) == 2000
 
def test_initialize_IS_misc_taxes():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.misc_taxes[-1])) == 1013

def test_initialize_IS_ebit():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.ebit[hist-1])) == 3886
    assert int(round(ut.ebit[-1])) == 4899

def test_initialize_IS_afudc():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.afudc[-1])) == 200
 
def test_initialize_IS_baseline_interest():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.baseline_interest[hist-1])) == 1000
    assert int(round(ut.baseline_interest[-1])) == 1000
 
def test_initialize_IS_ebt():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.ebt[hist-1])) == 3086
    assert int(round(ut.ebt[-1])) == 4099

def test_initialize_IS_income_taxes():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.income_tax[hist-1])) == 1034
    assert int(round(ut.income_tax[-1])) == 1373
 
def test_initialize_IS_net_income():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    assert int(round(ut.net_income[hist-1])) == 2052
    assert int(round(ut.net_income[-1])) == 2726

def test_initialize_CFS_capex():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    ut.initialize_CFS()
    assert int(round(ut.capex[-1])) == 5376

def test_initialize_CFS_shares_outstanding():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    ut.initialize_CFS()
    assert int(round(ut.shares_outstanding[-1])) == 1000

def test_initialize_CFS_dividends_paid():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    ut.initialize_CFS()
    assert int(round(ut.dividends_paid[-1])) == 1363

def test_initialize_CFS_DPS():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    ut.initialize_CFS()
    assert round(ut.dps[hist-1], 2) == 1.03
    assert round(ut.dps[-1], 2) == 1.36


## TEST PROJECT BUILD FUNCTIONS

def test_incremental_spend_total_no_esc_no_delay():
    npp = Project()
    assert round(npp.incremental_spend(0, npp.duration), 6) == 6000

def test_incremental_spend_half_no_esc_no_delay():
    npp = Project()
    assert round(npp.incremental_spend(0, 0.5*npp.duration), 6) == 3000

def test_incremental_spend_total_no_esc_w_delay():
    npp = Project()
    npp.delay_schedule()
    assert round(npp.incremental_spend(0, npp.duration), 6) == 6000

def test_incremental_spend_half_no_esc_w_delay():
    npp = Project()
    npp.delay_schedule()
    assert round(npp.incremental_spend(0, 0.5*npp.duration), 6) == 3000

def test_seek_alpha_iteratively():
    npp = Project()
    with open("./data/profiles/alpha-checkfile.csv", "r") as cf:
        alpha_data = csv.reader(cf, delimiter = ",", quotechar = "\"")
        for row in alpha_data:
            npp.epsilon = float(row[0])
            npp.duration = float(row[1])
            npp.seek_alpha()
            assert round(npp.alpha, 5) == round(float(row[2]), 5)
            #assert npp.alpha <= 1.00001 * float(row[2])
            #assert npp.alpha >= 0.99999 * float(row[2])

def test_incremental_spend_total_w_esc_w_delay():
    for i in range(50):
        npp = Project()
        npp.delay_schedule()
        npp.escalate_cost()
        assert npp.incremental_spend(0, npp.duration) >= 0.99*6000*(1+npp.epsilon)
        assert npp.incremental_spend(0, npp.duration) <= 1.01*6000*(1+npp.epsilon)

def test_spend_profile_d75_e08():
    ut = Utility("check", time_horizon, hist)
    npp = Project()
    npp.duration = 7.5
    npp.epsilon = 0.8
    npp.seek_alpha()
    npp.spend_profile(ut)
    cs_check = [286.52298, 1210.6903, 2784.41805, 4876.66361, 7193.50904, 9288.21863, 10609.39066, 10799.99999]
    ii_check = [10.02830, 42.7252, 99.30100, 176.00513, 263.25490, 345.78366, 404.12711, 212.47144]
    ci_check = [10.02830, 52.75346, 152.05446, 328.05959, 591.31449, 937.09815, 1341.22526, 1553.69670]
    for i in range(int(m.ceil(npp.duration))):
        assert round(npp.cum_spend[i], 3) == round(cs_check[i], 3)
        assert round(npp.inc_idc[i], 3) == round(ii_check[i], 3)
        assert round(npp.cum_idc[i], 3) == round(ci_check[i], 3)

def test_spend_profile_d149_e29():
    ut = Utility("check", time_horizon, hist)
    npp = Project()
    npp.duration = 14.9
    npp.epsilon = 2.9
    npp.seek_alpha()
    npp.spend_profile(ut)
    cs_check = [74.16361, 327.81021, 809.33618, 1566.79661, 2643.73789, 4073.79061, 5873.99551, 8036.93080, 10521.83645, 13245.09129, 16070.59111, 18800.79729, 21169.46783, 22837.33448, 23400.00000]
    ii_check = [2.59573, 11.56421, 28.82236, 56.34226, 96.00719, 149.41928, 217.65613, 300.97683, 398.48272, 507.74353, 624.40705, 741.81851, 850.68563, 938.83496, 892.24873]
    ci_check = [2.59573, 14.15993, 42.98230, 99.32456, 195.33175, 344.75103, 562.40716, 863.38399, 1261.86670, 1769.61023, 2394.01728, 3135.83579, 3986.52141, 4925.35637, 5817.60510]
    for i in range(int(m.ceil(npp.duration))):
        assert round(npp.cum_spend[i], 3) == round(cs_check[i], 3)
        assert round(npp.inc_idc[i], 3) == round(ii_check[i], 3)
        assert round(npp.cum_idc[i], 3) == round(ci_check[i], 3)


## INCORPORATE PROJECT INTO FSs

def test_incorporate_deterministic_project_interest():
    ut = Utility("check", time_horizon, hist)
    ut.initialize_IS()
    ut.initialize_CFS()
    npp = Project()
    npp.duration = 8.0
    npp.epsilon = 2.0
    npp.seek_alpha()
    npp.spend_profile(ut)
    npp.annual_capital_payment = npp.total_cost * mcd / (1 - (1+mcd)**(-term))
    ut.finance_project(npp)
    ut.incorporate_project(npp)
    ut.refresh_IS(0)
    ut.refresh_CFS(npp, 0)

    check_interest = np.zeros(time_horizon + hist)
    check_ebt = np.zeros(time_horizon + hist)
    check_income_tax = np.zeros(time_horizon + hist)
    check_net_income = np.zeros(time_horizon + hist)

    with open('./data/profiles/omnibus-checkfile-static.csv', 'r') as df:
        data = csv.reader(df, delimiter = ',', quotechar = '\"')
        for row in data:
            check_interest[:int(m.ceil(npp.duration))] = row[1:int(m.ceil(npp.duration))+1] if row[0] == 'PostInterestExpense' else check_interest[:int(m.ceil(npp.duration))]
            check_ebt[:int(m.ceil(npp.duration))] = row[1:int(m.ceil(npp.duration))+1] if row[0] == 'PostEBT' else check_ebt[:int(m.ceil(npp.duration))]
            check_income_tax[0:] = row[1:] if row[0] == 'PostIncomeTax' else check_income_tax
            check_net_income[0:] = row[1:] if row[0] == 'PostNetIncome' else check_net_income

    assert round(ut.interest[5], 3) == round(check_interest[5], 3)
    assert round(ut.ebt[5], 3) == round(check_ebt[5], 3)
    assert round(ut.income_tax[5], 3) == round(check_income_tax[5], 3)
    assert round(ut.net_income[5], 3) == round(check_net_income[5], 3)



