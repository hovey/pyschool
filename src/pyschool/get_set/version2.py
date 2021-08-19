# Version 2


class Celsius:

    MIN_C_VALUE = -273.15  # constant, designated with ALL CAPS

    def __init__(self, temperature=0.0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32.0

    # getter
    def get_temperature(self):
        return self._temperature

    # setter
    def set_temperature(self, value):

        if value < self.MIN_C_VALUE:
            raise ValueError(
                f"Temperature cannot be set to a value below {self.MIN_C_VALUE} degrees C."
            )
        else:
            self._temperature = value
