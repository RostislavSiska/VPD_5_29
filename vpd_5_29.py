"vpd_5_29"

from math import factorial

def row_sin(x, end=1000):
    "row Maklorena for sinx"
    summ = 0
    for i in range (end):
        summ = summ + (((-1)**i) * ((x**(2*i+1))/(factorial(2*i+1))))
    return summ

print(row_sin(9))
