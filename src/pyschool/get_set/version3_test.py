from version3 import Celsius

c = Celsius()

print(f'The default temperature is {c.temperature} degrees C.')
f = c.to_fahrenheit()
print(f'The default converted temperature is {f} degrees F.')

# Now overrite the original value with a new value
c.temperature = 100.0
print(f'The default temperature is {c.temperature} degrees C.')
f = c.to_fahrenheit()
print(f'The default converted temperature is {f} degrees F.')

# c3 = Celsius(-500.0) # this will cause an exception when uncommented, try it!
