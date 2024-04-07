# Import libraries
import numpy as np

def sehnen_trapez_regel(f, a, b, n):
    # Initialise
    dx = (b - a) / n
    x0 = a
    ST = 0

    # Sum up
    for i in range(n):
        # The Formulas
        x_n = x0 + i * dx
        x_n_1 = x0 + (i + 1) * dx  # this is the x_n+1 term
        ST_n = (x_n_1 - x_n) * (f(x_n) + f(x_n_1)) / 2

        ST += ST_n
        # intermediate results
        # print(f" ST_n at {i} is {ST_n} x_n is {x_n} x_n_1 is {x_n_1}")

    return ST

# print(f" The area calculated with ST is {sehnen_trapez_regel(f, a, b, n)}")

def tangenten_trapez_regel(f, a, b, n):
    # Initialise
    dx = (b - a) / n
    x0 = a
    TT = 0

    # Sum up
    for i in range(n):
        # The Formulas
        x_n = x0 + i * dx
        x_n_1 = x0 + (i + 1) * dx  # this is the x_n+1 term
        TT_n = (x_n_1 - x_n) * f((x_n_1 + x_n) / 2)

        TT += TT_n
        # intermediate results
        # print(f" TT_n at {i} is {TT_n} x_n is {x_n} x_n_1 is {x_n_1}")

    return TT

# print(f" The area calculated with TT is {tangenten_trapez_regel(f, a, b, n)}")

# Return Sn: = (ST_n+2⋅TT_n)/3

def simpson_regel(f, a, b, n):
    return (sehnen_trapez_regel(f, a, b, n) + 2 * tangenten_trapez_regel(f, a, b, n)) / 3

# print(f" The area calculated with Sn is {simpson_regel(f, a, b, n)}")

def Approx3(f, a, b, n):
    print(f" The area calculated with ST is {sehnen_trapez_regel(f, a, b, n)}")
    print(f" The area calculated with TT is {tangenten_trapez_regel(f, a, b, n)}")
    print(f" The area calculated with Sn is {simpson_regel(f, a, b, n)}")
    return " "


# Define funcitions
def f1(x):
    return np.sin(x)


def f2(x):
    return np.sqrt(1 - x ** 2)


def f3(x):
    return x ** 2


# Get the aproximatet integral with different n's
print("Integrate Sin(x) from  0 to pi")
for n in [1, 2, 3, 5, 10, 99999]:
    print(f"n={n}")
    print(f" {Approx3(f1, 0, np.pi, n)}")

print("Integrate sqrt(1-x**2) from  -1 to 1")
for n in [1, 2, 3, 5, 10, 99999]:
    print(f"n={n}")
    print(f" {Approx3(f2, -1, 1, n)}")

print("Integrate x^2 from  0 to 1")
for n in [1, 2, 3, 5, 10, 99999]:
    print(f"n={n}")
    print(f" {Approx3(f3, 0, 1, n)}")

from sympy import *

x = symbols('x')

#1
res1 = integrate( sin(x), (x, 0, pi))
res2 = integrate( sqrt(1-x**2), (x ,-1 , 1 ))
res3 = integrate( x**2, (x, 0, 1))

print(f"integrate( sin(x), (x, 0, pi)) is  = {res1}")
print(f"integrate( sqrt(1-x**2), (x ,-1 , 1 )) is  = {res2}")
print(f"integrate( x**2, (x, 0, 1)) is  = {res3}")


def Error3(f, a, b, n, res):
    er_ST = res - sehnen_trapez_regel(f, a, b, n)
    er_TT = res - tangenten_trapez_regel(f, a, b, n)
    er_Sn = res - simpson_regel(f, a, b, n)

    er_ST = er_ST.evalf()
    er_TT = er_TT.evalf()
    er_Sn = er_Sn.evalf()

    print(f" The error calculated with ST is {er_ST}")
    print(f" The error calculated with TT is {er_TT}")
    print(f" The error calculated with Sn is {er_Sn}")
    return " "


print("Integrate Sin(x) from  0 to pi")
for n in [1, 2, 3, 5, 10, 99999]:
    print(f"n={n}")
    print(f" {Error3(f1, 0, np.pi, n, res1)}")

print("Integrate sqrt(1-x**2) from  -1 to 1")
for n in [1, 2, 3, 5, 10, 99999]:
    print(f"n={n}")
    print(f" {Error3(f2, -1, 1, n, res2)}")

print("Integrate x^2 from  0 to 1")
for n in [1, 2, 3, 5, 10, 99999]:
    print(f"n={n}")
    print(f" {Error3(f3, 0, 1, n, res3)}")