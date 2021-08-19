vehicles = ["Chevy", "Ford", "Chrysler"]

# Before
print("The cars we have for sale today are:")
i = 0  # index
for i in range(0, len(vehicles)):
    print(f"  {vehicles[i]}")
    i += 1

# After
print("The cars we have for sale today are:")
for vehicle in vehicles:
    print(f"  {vehicle}")
