'''Voltage formula'''

import numpy as np

V_0 = 10
a = 2.5
z = 13.0/3.0

V = V_0 * (1 - (z/(a**2 + z**2)**0.5))

print(f'First voltage is {V}')

z = 26.0/3

V = V_0 * (1 - (z/(a**2 + z**2)**0.5))
print(f'Second voltage is {V}')

z = 13

V = V_0 * (1 - (z/(a**2 + z**2)**0.5))
print(f'Third voltage is {V}')