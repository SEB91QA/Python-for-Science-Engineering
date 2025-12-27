# Get inputs

distance = 180.
mpk = 3.9
speed = 60.
cost_per_kWh = 0.22

# Calculate outputs
time = distance / speed
energy = distance / mpk
cost = energy * cost_per_kWh

#Print outputs
print(time)
print(energy)
print(cost)