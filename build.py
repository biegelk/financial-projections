import math as m
import numpy as np
from constants import *
import random as rand

class Project:
    """ Project class contains plant attributes and project outcomes """

    def __init__(self, rand_delay):
        # Construction outcomes
        self.initial_cost = total_cost
        self.total_cost = self.initial_cost
        if rand_delay:
            self.duration = init_schedule * (1+rand.random())
        else:
            self.duration = init_schedule
        self.inc_spend = np.zeros(m.ceil(self.duration))
        self.cum_spend = np.zeros(m.ceil(self.duration))
        self.idc = np.zeros(m.ceil(self.duration))
        self.annual_capital_payment = 0.0
        self.capital_npv = 0
        self.npv = 0

        # Operational outcomes
        self.annual_generation = capacity * cf * 8766.0 # kWh/yr
        self.annual_fuel_cost = 151.0 # $M/yr
        self.annual_om_cost = 139.0   # $M/yr
        self.annual_revenue = power_price * self.annual_generation / 1e6
        self.lcoe = 0.0
        self.revenue_npv = 0
        self.fuel_npv = 0
        self.om_npv = 0


    def spend_profile(self, cap_interest):
        # Set incremental spend
        for i in range(m.floor(self.duration)):
            self.inc_spend[i] = self.total_cost*(-1/2)*(m.cos(m.pi*(i+1)/self.duration) - m.cos(m.pi*i/self.duration))
        self.inc_spend[-1] = self.total_cost - np.sum(self.inc_spend[:-1])

        # Tally cumulative spend
        for i in range(m.ceil(self.duration)):
            for j in range(m.ceil(self.duration)):
                if j >= i:
                    self.cum_spend[j] += self.inc_spend[i]

        # If capitalizing interest, add IDC to year 0's project spend
        self.cum_spend[0] += self.cum_spend[0]/2 * mcd if cap_interest else self.cum_spend[0]
        for i in range(1,m.ceil(self.duration)):
            self.idc[i] = (self.cum_spend[i]+self.cum_spend[i-1])/2 * mcd
            # If we're capitalizing interest, add IDC to each year's project spend
            self.cum_spend[i] += self.idc[i] if cap_interest else self.cum_spend[i]

        # Update total final project cost
        self.total_cost = self.cum_spend[-1]

        print("duration = ", self.duration)
        print("total cost = ", self.total_cost)




    def build_plant(self, cap_interest):
        self.spend_profile(cap_interest)
        self.annual_capital_payment = self.total_cost * mcd / (1 - (1+mcd)**(-term))


    def get_lcoe(self):
        self.lcoe = 100000000*(self.annual_capital_payment + self.annual_fuel_cost + self.annual_om_cost) / self.annual_generation


    def get_npv(self):
        # NPV contributions during debt repayment period
        for i in range(term):
            self.capital_npv += self.annual_capital_payment / (1+d)**i
            self.revenue_npv += self.annual_revenue / (1+d)**i
            self.fuel_npv += self.annual_fuel_cost / (1+d)**i
            self.om_npv += self.annual_om_cost / (1+d)**i
        # NPV contributions after debt is repaid
        for i in range(term, life):
            self.revenue_npv += self.annual_revenue / (1+d)**i
            self.fuel_npv += self.annual_fuel_cost / (1+d)**i
            self.om_npv += self.annual_om_cost / (1+d)**i
        # Total NPV
        self.npv = self.revenue_npv - self.capital_npv - self.fuel_npv - self.om_npv 









