'''Quadratic equation'''

import numpy as np

a = input("Please enter the value of a: ")
b = input("Please enter the value of b: ")
c = input("Please enter the value of c: ")

x_1 = (-b + np.sqrt(b**2 - 4 * a * c))/(2*a)
x_2 = (-b - np.sqrt(b**2 - 4 * a * c))/(2*a)

print("First ")