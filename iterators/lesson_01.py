vehicle_types_list = ["Chevy", "Ford", "Chrysler"]

# Before
print("The cars we have for sale today are:")
i = 0  # index
for i in range(0, len(vehicle_types_list)):
    print(f"  {vehicle_types_list[i]}")
    i += 1

# After
print("The cars we have for sale today are:")
for vehicle in vehicle_types_list:
    print(f"  {vehicle}")
