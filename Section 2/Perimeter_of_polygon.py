'''Perimeter of a polygon inscribed in a circle'''

import numpy as np

n = 3
p = n * np.sin(np.pi/n)

print(f"The perimeter of the {n}-gon is: {p}") 

n = 4
p = n * np.sin(np.pi/n)

print(f"The perimeter of the {n}-gon is: {p}") 

n = 5
p = n * np.sin(np.pi/n)

print(f"The perimeter of the {n}-gon is: {p}") 

n = 100
p = n * np.sin(np.pi/n)

print(f"The perimeter of the {n}-gon is: {p}") 

n = 10000
p = n * np.sin(np.pi/n)

print(f"The perimeter of the {n}-gon is: {p}") 

n = 1000000
p = n * np.sin(np.pi/n)

print(f"The perimeter of the {n}-gon is: {p}") 