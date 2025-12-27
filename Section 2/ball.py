'''Ball thrown vertically'''


g = 9.8
h_0 = 1.6
v_0 = 14.2
t = 2.0

h = h_0 + v_0 * t - (1/2)*g*t**2
v = v_0 - g*t


print("Height and velocity at t = 2s\n")
print(h)
print(v) 