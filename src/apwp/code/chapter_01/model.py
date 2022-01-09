"""Implements the order and batch."""

from datetime import date
from typing import NamedTuple, Set


class OrderLine(NamedTuple):
    """A single line from an order.

    Attributes:
        id (int): The order ID to which the orderline belongs.
        quantity (int): The number of units of SKU to order.
        sku (str): The stock-keeping unit.
    """

    id: int
    quantity: int
    sku: str


class Batch:
    """Records the amount of a given SKU and when it will arrive at the warehouse.

    Attributes:
        eta (date): The date at which the batch will arrive at the warehouse. Set to
            date.today() if it is in the warehouse.
        quantity (int): How many units are in the batch.

    Keyword Attributes:
        eta (date): The date at which the batch will arrive at the warehouse. Set to
            date.today() if it is in the warehouse.
        quantity (int): How many units are in the batch.
        reference (str): A unique identifier for batches.
        sku (str): The stock-keeping unit.
    """

    def __init__(self, *, eta: date, quantity: int, reference: str, sku: str):
        self.eta = eta
        self.quantity = quantity
        self.__reference = reference
        self.__sku = sku
        self._allocations = set()  # type: Set[OrderLine]

    def allocate(self, *, line: OrderLine) -> bool:
        """Try to allocate the line to the batch.

        Keyword Arguments:
            line (OrderLine): The order line to try to allocate to the batch.

        Returns:
            allocated (bool): True if the order line was successfully allocated to the
                batch.

        Examples:
            >>> line = OrderLine(id=0, sku="table", quantity=5)
            >>> batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())
            >>> batch.allocate(line=line)
            True
            >>> batch.quantity = 5

            >>> line = OrderLine(id=0, sku="table", quantity=15)
            >>> batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())
            >>> batch.allocate(line=line)
            False
            >>> batch.quantity = 10
        """
        too_many_units = line.quantity > self.quantity
        wrong_sku = line.sku != self.sku
        already_added = line in self._allocations
        if too_many_units or wrong_sku or already_added:
            return False

        self._allocations.add(line)
        self.quantity -= line.quantity
        return True

    def deallocate(self, *, line: OrderLine) -> bool:
        """Try to deallocate the line from the batch.

        Keyword Arguments:
            line (OrderLine): The order line to try to deallocate to the batch.

        Returns:
            deallocated (bool): True if the order line was successfully deallocated from
                the batch.

        Examples:
            >>> line = OrderLine(id=0, sku="table", quantity=5)
            >>> batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())
            >>> batch.deallocate(line=line)
            False
            >>> batch.quantity = 10
            >>> batch.allocate(line=line)
            True
            >>> batch.quantity
            5
            >>> batch.deallocate(line=line)
            True
            >>> batch.quantity
            10
        """
        if line in self._allocations:
            self.quantity += line.quantity
            self._allocations.remove(line)
            return True

        return False

    def __lt__(self, other):
        """Enable sorting by ETA."""
        return self.eta < other.eta

    @property
    def reference(self) -> str:
        """A unique identifier for batches."""
        return self.__reference

    @property
    def sku(self) -> str:
        """The stock-keeping unit."""
        return self.__sku


def allocate(*, batches=tuple[Batch, ...], line: OrderLine) -> bool:
    """Allocate the line to the earliest batch.

    Keyword Arguments:
        batches (tuple[Batch, ...]): The batches to which to try to allocate the line.
        line (OrderLine): The order line to try to allocate.

    Returns:
        allocated (bool): If true, the line order was allocated to a batch.

    Examples:
    >>> today = date.today()
    >>> tomorrow = today + timedelta(days=1)
    >>> line = OrderLine(id=0, sku="table", quantity=10)
    >>> warehouse = Batch(quantity=10, reference="warehouse", sku="table", eta=today)
    >>> en_route = Batch(quantity=10, reference="en_route", sku="table", eta=tomorrow)
    >>> allocate(line=line, batches=(en_route, warehouse))
    True
    >>> en_route.quantity
    10
    >>> warehouse.quantity
    0
    """
    sorted_batches = sorted(batches)
    allocated = False
    for batch in sorted_batches:
        allocated = batch.allocate(line=line)
        if allocated:
            break

    return allocated
