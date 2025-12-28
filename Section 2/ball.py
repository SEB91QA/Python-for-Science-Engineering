'''Ball thrown vertically'''


g = 9.8
h_0 = 1.6
v_0 = 14.2
t = 0.5

h = h_0 + v_0 * t - (1/2)*g*t**2
v = v_0 - g*t


print("Height and velocity at t = 0.5s:\n")
print(f'{h}m')
print(f'{v}m/s') 

t = 2

h = h_0 + v_0 * t - (1/2)*g*t**2
v = v_0 - g*t


print('\nHeight and velocity at t = 2s:\n')
print(f'{h}m')
print(f'{v}m/s') 