# attributes.py

from abc import ABC, abstractmethod

# Attribute Service


class Attribute(ABC):
    def __init__(self):
        super().__init__()
        self._name = "Attribute (abstract)"
        self.announcement()

    def announcement(self):
        print(f"This is the {self._name} class")


class Color(Attribute):
    def __init__(self, R=0.5, G=0.5, B=0.5):
        super().__init__()
        rgb(self, R, G, B)
        self._name = "Color (attribute)"
        self.announcement()

    @property
    def rgb(self):
        return self._r, self._g, self._b

    @rgb.setter
    def rgb(self, R, G, B):
        if R >= 0 and G >= 0 and B >= 0:
            self._r, self._g, self._b = R, G, B
        else:
            raise ValueError(
                "All RGB values must be non-negative.  No change to existing RBG color."
            )
