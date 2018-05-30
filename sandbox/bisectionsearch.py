import math as m
from random import *
import csv

def seek_alpha_draft(duration, epsilon):
    alpha = 0.1
    i = 1.0
    while i < 100:
        print("i = ", i)
        print("alpha = ", alpha)
        if m.exp(alpha*duration) - 2*(1+epsilon)*alpha**2 * duration**2/(m.pi**2) >= 1.01 * (2*(1+epsilon) -1):
            alpha = alpha * (1 - 2/(i + 1.2))
            i += 1
        elif m.exp(alpha*duration) - 2*(1+epsilon)*alpha**2 * duration**2/(m.pi**2) <= 0.99 * (2*(1+epsilon) -1):
            alpha = alpha * (1 + 1/i)
            i += 1 
        else:
            break
    return alpha


def a_func(alpha, duration, epsilon):
    return m.exp(float(alpha) * float(duration)) - 2*(1+float(epsilon))*(float(alpha)**2)*(float(duration)**2)/(m.pi**2) - 2*(1+float(epsilon)) + 1


def seek_alpha_bisection(duration, epsilon, amin, amax):
    alpha = 1.0
    result = 0.0
    i = 1
    a = amin
    b = amax
    while i < 250:
        c = (float(a) + float(b)) / 2.
        print("c =", c)
        result = a_func(c, duration, epsilon)
        print(result)
        if round(result,6) == 0:
            alpha = c
            break
        elif result < 0:
            a = c
            i += 1
        else:
            b = c
            i += 1
    alpha = c
    print("alpha =", c)
    return alpha



#def test_seek_alpha_draft_iteratively():
#    with open("./alpha-checkfile.csv", "r") as cf:
#        alpha_data = csv.reader(cf, delimiter = ",", quotechar = "\"")
#        for row in alpha_data:
#            assert seek_alpha_draft(row[1], row[0]) >= 0.99 * row[2]
#            assert seek_alpha_draft(row[1], row[0]) <= 1.01 * row[2]

def test_seek_alpha_bisection():
    with open("./alpha-2-checkfile.csv", "r") as cf:
        alpha_data = csv.reader(cf, delimiter = ",", quotechar = "\"")
        for row in alpha_data:
            assert seek_alpha_bisection(row[1], row[0], 0, 2) >= 0.9999 * row[2]
            assert seek_alpha_bisection(row[1], row[0], 0, 2) <= 1.0001 * row[2]
