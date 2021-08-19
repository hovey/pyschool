# Version 3


class Celsius:

    MIN_C_VALUE = -273.15  # constant, designated with ALL CAPS

    def __init__(self, temperature=0.0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32.0

    # getter
    @property
    def temperature(self):  # formerly get_temperature(self):
        print(
            f"The getter was called."
        )  # done just so clients can see the getter is called.
        return self._temperature

    # setter
    @temperature.setter
    def temperature(self, value):
        print(
            f"The setter was called."
        )  # done just so clients can see the setter is called.

        if value < self.MIN_C_VALUE:
            raise ValueError(
                f"Temperature cannot be set to a value below {self.MIN_C_VALUE} degrees C."
            )
        else:
            self._temperature = value
