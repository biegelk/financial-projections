import math as m
import numpy as np

def build_plant(total_cost, duration):
    inc_spend = np.zeros(duration)
    cum_spend = np.zeros(duration)
    for i in range(duration):
        inc_spend[i] = total_cost / duration
        cum_spend[i:] += total_cost / duration
    return (inc_spend, cum_spend)

#def npv(total_cost, duration, mcd, term)
