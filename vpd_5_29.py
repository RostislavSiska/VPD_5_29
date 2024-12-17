"vpd_5_29"

from math import factorial
from decimal import Decimal

def row_sin(x, end=1000):
    "row Maklorena for sinx"
    summ = 0
    for i in range(end):
        summ = summ + (((-1)**i) * ((x**(2*i + 1))/(factorial(2*i + 1))))
    return summ

print(row_sin(9))

def row_chx(x, end=1000):
    "row Maklorena for chx"
    summ = 0
    for i in range(end):
        summ = summ + ((x**(2*i))/(factorial(2*i)))
    return summ

print(row_chx(Decimal(10)))
