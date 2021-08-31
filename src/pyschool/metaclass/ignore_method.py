"""Example use of metaclasses. Ignore a method implementation."""

# Reference: https://stackoverflow.com/questions/18858759/python-decorating-a-class-method-that-is-intended-to-be-overwritten-when-inheri


class Chores:
    """Default chores implementation."""

    def __init__(self):
        pass

    def clean(self):
        """When cleaning."""
        print("I am cleaning!")

    def garden(self):
        """When gardening."""
        print("I am gardening!")

    def laundry(self):
        """When doing laundry."""
        print("I am doing laundry!")


class LazyChoresMeta(type):
    """Meta class to ignore certain chores."""

    def __init__(cls, name, bases, clsdict):
        banned_methods = ["clean", "garden"]
        for mthd in banned_methods:

            def do_nothing(self):
                pass

            setattr(cls, mthd, do_nothing)


class LazyChores(Chores, metaclass=LazyChoresMeta):
    """Ignore cleaning and gardening."""

    def __init__(self):
        super().__init__()


class TryingNotToBeLazy(Chores, metaclass=LazyChoresMeta):
    """Try to implement cleaning and gardening."""

    def __init__(self):
        super().__init__()

    def clean(self):
        """When cleaning. This should not print."""
        print("I am lazily cleaning!")

    def garden(self):
        """When gardening. This should not print."""
        print("I am lazily gardening!")

    def laundry(self):
        """When doing laundry. This should print."""
        print("I am doing lazily laundry!")


if __name__ == "__main__":
    print("chores")
    chores = Chores()
    chores.clean()
    chores.garden()
    chores.laundry()

    print("\nlazy chores")
    lazy_chores = LazyChores()
    lazy_chores.clean()
    lazy_chores.garden()
    lazy_chores.laundry()

    print("\ntrying not to be lazy chores")
    not_lazy_chores = TryingNotToBeLazy()
    not_lazy_chores.clean()
    not_lazy_chores.garden()
    not_lazy_chores.laundry()
