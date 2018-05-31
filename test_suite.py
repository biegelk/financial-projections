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
    assert npp.incremental_spend(0, npp.duration) == 6000

def test_incremental_spend_half_no_esc_no_delay():
    npp = Project()
    assert npp.incremental_spend(0, 0.5*npp.duration) == 3000

def test_incremental_spend_total_no_esc_w_delay():
    npp = Project()
    npp.delay_schedule()
    assert npp.incremental_spend(0, npp.duration) == 6000

def test_incremental_spend_half_no_esc_w_delay():
    npp = Project()
    npp.delay_schedule()
    assert npp.incremental_spend(0, 0.5*npp.duration) == 3000

def test_seek_alpha_iteratively():
    npp = Project()
    with open("./data/profiles/alpha-checkfile.csv", "r") as cf:
        alpha_data = csv.reader(cf, delimiter = ",", quotechar = "\"")
        for row in alpha_data:
            npp.epsilon = float(row[0])
            npp.duration = float(row[1])
            npp.seek_alpha()
            assert npp.alpha <= 1.00001 * float(row[2])
            assert npp.alpha >= 0.99999 * float(row[2])

def test_incremental_spend_total_w_esc_w_delay():
    for i in range(50):
        npp = Project()
        npp.delay_schedule()
        npp.escalate_cost()
        assert npp.incremental_spend(0, npp.duration) >= 0.99*6000*(1+npp.epsilon)
        assert npp.incremental_spend(0, npp.duration) <= 1.01*6000*(1+npp.epsilon)



