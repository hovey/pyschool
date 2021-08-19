from version2 import Celsius

c = Celsius()

print(f"The default temperature is {c.get_temperature()} degrees C.")
f = c.to_fahrenheit()
print(f"The default converted temperature is {f} degrees F.")

c2 = Celsius(37.0)  # set default temperature to human body temperature
print(f"The body temperature is {c2.get_temperature()} degrees C.")
# Here we show clients can circumvent the Celcius.get_temperature() API
print(f"The body temperature, via private data access, is {c2._temperature} degrees C.")
f2 = c2.to_fahrenheit()
print(f"The body converted temperature is {f2} degrees F.")

print("The dictionary of the object is:")
print(c2.__dict__)

# c3 = Celsius(-500.0) # this will cause an exception when uncommented, try it!
