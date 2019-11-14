from version1 import Celsius

c = Celsius()

print(f'The default temperature is {c.temperature} degrees C.')
f = c.to_fahrenheit()
print(f'The default converted temperature is {f} degrees F.')

c2 = Celsius(37.0) # set default temperature to human body temperature
print(f'The body temperature is {c2.temperature} degrees C.')
f2 = c2.to_fahrenheit()
print(f'The body converted temperature is {f2} degrees F.')

print('The dictionary of the object is:')
print(c2.__dict__)