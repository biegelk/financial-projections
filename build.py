import math as m
import numpy as np
from constants import *
import random as rand

class Project:
    """ Project class contains plant attributes and project outcomes """

    def __init__(self):
        # Behavioral booleans
        self.rand_esc = rand_esc
        self.rand_delay = rand_delay
        self.cap_interest = cap_interest

        # Construction outcomes
        self.initial_cost = total_cost
        self.init_schedule = init_schedule
        # Default values in case probabilistic execution is turned off
        self.total_cost = self.initial_cost
        self.duration = init_schedule

        self.stage_durations = np.ones(self.init_schedule) * float(self.init_schedule) / 5.
        self.stage_escalation = 5*np.ones(5) # placeholder values to enforce cap on np.random.gamma values
        self.annual_capital_payment = 0.0
        self.capital_npv = 0
        self.npv = 0
        self.max_delay = 3.0
        self.alpha = 0.
        self.epsilon = 2
        self.a = 0.0
        self.b = 0.0

        # Operational outcomes
        self.annual_generation = capacity * cf * 8766.0 # kWh/yr
        self.annual_fuel_cost = 151.0 # $M/yr
        self.annual_om_cost = 139.0   # $M/yr
        self.annual_revenue = power_price * self.annual_generation / 1e6
        self.lcoe = 0.0
        self.revenue_npv = 0
        self.fuel_npv = 0
        self.om_npv = 0


    def incremental_spend(self, T1, T2):
        #return (m.exp(self.alpha*T2)*(self.alpha*self.duration*m.sin(m.pi*T2/self.duration)-m.pi*m.cos(m.pi*T2/self.duration))/(self.alpha**2*self.duration**2 + m.pi**2) - m.exp(self.alpha*T1)*(self.alpha*self.duration*m.sin(m.pi*T1/self.duration) - m.pi*m.cos(m.pi*T1/self.duration))/(self.alpha**2*self.duration**2+m.pi**2))
        return self.total_cost*m.pi/2. * (m.exp(self.alpha*T2)*(self.alpha*self.duration*m.sin(m.pi*T2/self.duration)-m.pi*m.cos(m.pi*T2/self.duration))/(self.alpha**2*self.duration**2 + m.pi**2) - m.exp(self.alpha*T1)*(self.alpha*self.duration*m.sin(m.pi*T1/self.duration) - m.pi*m.cos(m.pi*T1/self.duration))/(self.alpha**2*self.duration**2+m.pi**2))
        

    def delay_schedule(self):
        if rand_delay:
            self.duration = self.init_schedule * (1. + np.random.gamma(sgamma_params[0], sgamma_params[1]) - sgamma_deshift)
        while self.duration >= 15:
            self.duration = self.init_schedule * (1. + np.random.gamma(sgamma_params[0], sgamma_params[1]) - sgamma_deshift)


    def alpha_func(self, alpha, duration, epsilon):
        return m.exp(float(alpha) * float(duration)) - 2*(1+float(epsilon))*(float(alpha)**2)*(float(duration)**2)/(m.pi**2) - 2*(1+float(epsilon)) + 1


    def seek_alpha(self):
        '''Bisection search implementation'''
        self.alpha = 0.1
        result = 0.0
        i = 1.0
        a = amin
        b = amax
        while i < 500:
            c = (float(a) + float(b)) / 2.
            result = self.alpha_func(c, self.duration, self.epsilon)
            if round(result, 8) == 0:
                break
            elif result < 0:
                a = c
                i += 1
            else:
                b = c
                i += 1
        self.alpha = c
 

    def calculate_epsilon(self):
        self.epsilon = 0.0
        #while self.epsilon >= 2:
        #    self.epsilon = np.random.gamma(1.2, 0.6)


    def escalate_cost(self):
        self.calculate_epsilon()
        self.seek_alpha()


    def spend_profile(self, ut):
        # Initialize vectors for spend data
        # length = project duration (loaded into appropriate slots by Utility class functions)
        self.inc_spend = np.zeros(int(m.ceil(self.duration)))
        self.cum_spend = np.zeros(int(m.ceil(self.duration))) # only holds "overnight cost" spend, interest is tracked separately
        self.inc_idc   = np.zeros(int(m.ceil(self.duration)) + 1)
        self.cum_idc   = np.zeros(int(m.ceil(self.duration)) + 1)
        self.total_cum_spend = np.zeros(int(m.ceil(self.duration))) # holds sum of overnight cost and financing cost spend

        # Break known total cost into annual segments based on known duration
        # Complete expenditure years only:
        for i in range(int(m.floor(self.duration))):
            self.inc_spend[i] = self.incremental_spend(float(i), float(i+1))
            # each new incremental-spend slice contributes to running total for current and all later periods
            self.cum_spend[i:] += self.inc_spend[i]
        # End-of-project partial-year fragment
        self.inc_spend[-1] = self.incremental_spend(m.floor(self.duration), self.duration)
        self.cum_spend[-1] += self.inc_spend[-1]

        # Track financing costs, using ut's capital structure and assuming all interest is capitalized
        # Other years (EOP partial-year fragment poses no problem to incorporation here):
        for i in range(0,int(m.floor(self.duration))):
            self.inc_idc[i] = (self.cum_spend[i] + self.cum_idc[i]) * ut.debt_fraction * mcd
            self.cum_idc[i:] += self.inc_idc[i]
        # add impact of final year new inc_idc:
        self.inc_idc[-1] =  (self.cum_spend[-1] + self.cum_idc[-1]) * ut.debt_fraction * mcd * (self.duration - m.floor(self.duration))
        self.cum_idc[-1] += self.inc_idc[-1]


        # Total cumulative project spend tracker
#        self.total_cum_spend = np.add(self.cum_spend, self.cum_idc)

        # Update total final project cost
        self.total_cost = self.cum_idc[-1]
            



    def build_plant(self, ut):
        self.delay_schedule()
        self.escalate_cost()
        self.spend_profile(ut)
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









