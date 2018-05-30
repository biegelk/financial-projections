import math as m
from random import *
import csv

def seek_alpha(epsilon, duration):
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


# fails!
#def test_calculate_thing_01_50():
#    assert seek_alpha(0.1, 5.0) >= 0.99 * 0.037786
#    assert seek_alpha(0.1, 5.0) <= 1.01 * 0.037786

# passes
#def test_calculate_thing_05_90():
#    assert seek_alpha(0.5, 9.0) >= 0.99 * 0.086891604
#    assert seek_alpha(0.5, 9.0) <= 1.01 * 0.086891604

# passes
#def test_calculate_thing_09_60():
#    assert seek_alpha(0.9, 6.0) >= 0.99 * 0.20236877
#    assert seek_alpha(0.9, 6.0) <= 1.01 * 0.20236877

def test_seek_alpha_iteratively():
    with open("./alpha-checkfile.csv", "r") as cf:
        alpha_data = csv.reader(cf, delimiter = ",", quotechar = "\"")
        for row in alpha_data:
            assert seek_alpha(row[0], row[1]) >= 0.99 * row[2]
            assert seek_alpha(row[0], rpw[1]) <= 1.01 * row[2]

