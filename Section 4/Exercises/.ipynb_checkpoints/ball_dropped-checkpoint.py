'''Heigh and time for a ball dropped with zero velocity from a height h_0'''
import numpy as np
#  %precision 3

y = np.arange(10, 0, -0.5)
t = np.sqrt(2*(10 - y)/9.8)

print(y)
print(t)