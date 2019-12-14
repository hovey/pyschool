# Rectangles and Squares
# Squares are Rectangles.
# Rectangles are not Squares.
# The client asks the Shape Factor for Circles, but they are not provided
# by the Shape Service.
from abc import ABC, abstractmethod

# Shape Service

class Shape(ABC):

    def __init__(self, dx=1, dy=1):
        super().__init__()
        self._name = 'Shape (abstract)'
        print(self.name + f' constructor called with length={dx}, width={dy}.')
        self._dx = dx
        self._dy = dy

    def metrics(self):
        print(f'Metrics for {self.name}:')
        print(f'  x-dimension is {self.dx}.')
        print(f'  y-dimension is {self.dy}.')
        print(f'  area is {self.area()}.')
        print(f'  perimeter is {self.perimeter()}.\n')

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    @property
    def name(self): return self._name

    @name.setter
    def name(self, value): self._name = value

    @property
    def dx(self): return self._dx

    @dx.setter
    def dx(self, value):
        if value > 0:
            self._dx = value
        else:
            raise ValueError('Dimension cannot be set to a negative value.  No change to existing dimension.')

    @property
    def dy(self): return self._dy

    @dy.setter
    def dy(self, value):
        if value > 0:
            self._dy = value
        else:
            raise ValueError('Dimension cannot be set to a negative value.  No change to existing dimension.')


class Rectangle(Shape):
    def __init__(self, dx=1, dy=1):
    # def __init__(self):
        super().__init__(dx, dy)
        self.name = 'Rectangle'  # use the setter
        print(self.name + f' constructor called with length={dx}, width={dy}.')

    def area(self):  # override
        return self._dx * self._dy

    def perimeter(self):  # override
        return 2 * self._dx + 2 * self._dy


class Square(Rectangle):
    def __init__(self, dx=1):
        super().__init__(dx, dx)
        self.name = 'Square'  # use the setter
        print(self.name + f' constructor called with length={dx}.')

    @property
    def dx(self):
        return self._dx

    @dx.setter  # override
    def dx(self, value):
        self._dx = value
        self._dy = value  # enforce a square is always a square

    @property
    def dy(self):
        return self._dy

    @dy.setter  # override
    def dy(self, value):
        self._dy = value
        self._dx = value  # enforce a square is always a square

# Shape Factory

_items = {
    'rectangle': Rectangle,
    'square': Square
}

class ShapeFactory(object):

    @staticmethod
    def create(item):
        instance = _items.get(item, None)
        if instance:
            return instance()
        else:
            print(f'Warning: {item} requested but not provided by this factory, returning None.')
            return None

# Client

# The not-preferred way:
# Client manually creates concrete classes, which is bad.  Instead, the client
# should create a class through the Shape interface.
l, w = 2, 4
r = Rectangle()
r.metrics()

r = Rectangle(l, w)
r.metrics()

s = Square()
s.metrics()

s = Square(w)
s.metrics()

# The preferred way:
# Client now uses with a factory for object creation
sf = ShapeFactory()

r = sf.create('square')
r.metrics()

c = sf.create('circle')
# c.metrics()  # This will cause an error because c = None, clients may want to check for None, but 
               # there is a better way shown below.

# The better way:
items = ['rectangle', 'square', 'circle']
objects = []

for item in items:
    object = sf.create(item)
    if object:
        objects.append(object)
    else:
        print('Item is None from factory, so not added to Client object list.')

for object in objects:
    object.dx = 2
    # object.dy = -4  # will cause error, values must be positive
    object.metrics()
