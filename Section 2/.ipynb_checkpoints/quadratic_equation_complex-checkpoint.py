'''Quadratic equation with complex solutions'''

import numpy as np

a = float(input("Please enter the value of a: "))
b = float(input("Please enter the value of b: "))
c = float(input("Please enter the value of c: "))

a = a + 0j
b = b + 0j
c = c + 0j

x_1 = (-b + np.sqrt(b**2 - 4 * a * c))/(2*a)
x_2 = (-b - np.sqrt(b**2 - 4 * a * c))/(2*a)

print(f"First solution is: {x_1}")
print(f"Second solution is: {x_2}")