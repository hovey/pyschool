from datetime import date, timedelta
import pytest

from model import allocate, Batch, OrderLine

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_allocating_to_a_batch_reduces_the_available_quantity():
    # Given
    line = OrderLine(id=0, sku="table", quantity=5)
    batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())

    # When
    _ = batch.allocate(line=line)

    # Then
    assert batch.quantity == 5


def test_can_allocate_if_available_greater_than_required():
    # Given
    line = OrderLine(id=0, sku="table", quantity=5)
    batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())

    # When
    allocated = batch.allocate(line=line)

    # Then
    assert allocated


def test_cannot_allocate_if_available_smaller_than_required():
    # Given
    line = OrderLine(id=0, sku="table", quantity=15)
    batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())

    # When
    allocated = batch.allocate(line=line)

    # Then
    assert not allocated


def test_can_allocate_if_available_equal_to_required():
    # Given
    line = OrderLine(id=0, sku="table", quantity=10)
    batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())

    # When
    allocated = batch.allocate(line=line)

    # Then
    assert allocated
    assert batch.quantity == 0


def test_prefers_warehouse_batches_to_shipments():
    # Given
    today = date.today()
    tomorrow = today + timedelta(days=1)
    line = OrderLine(id=0, sku="table", quantity=10)
    warehouse = Batch(quantity=10, reference="warehouse", sku="table", eta=today)
    en_route = Batch(quantity=10, reference="en_route", sku="table", eta=tomorrow)

    # When
    _ = allocate(line=line, batches=(en_route, warehouse))

    # Then
    assert en_route.quantity == 10
    assert warehouse.quantity == 0


def test_prefers_earlier_batches():
    # Given
    today = date.today()
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(weeks=1)
    line = OrderLine(id=0, sku="table", quantity=10)
    early = Batch(quantity=10, reference="early", sku="table", eta=tomorrow)
    late = Batch(quantity=10, reference="late", sku="table", eta=next_week)

    # When
    _ = allocate(line=line, batches=(late, early))

    # Then
    assert late.quantity == 10
    assert early.quantity == 0


def test_cannot_allocate_if_sku_mismatch():
    # Given
    line = OrderLine(id=0, sku="table", quantity=5)
    batch = Batch(quantity=10, reference="test", sku="chair", eta=date.today())

    # When
    allocated = batch.allocate(line=line)

    # Then
    assert not allocated


def test_cannot_reallocate_existing_line():
    # Given
    line = OrderLine(id=0, sku="table", quantity=5)
    batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())

    # When
    _ = batch.allocate(line=line)
    allocated = batch.allocate(line=line)

    # Then
    assert not allocated


def test_can_deallocate_existing_line():
    # Given
    line = OrderLine(id=0, sku="table", quantity=5)
    batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())

    # When
    _ = batch.allocate(line=line)
    deallocated = batch.deallocate(line=line)

    # Then
    assert deallocated
    assert batch.quantity == 10


def test_cannot_deallocate_new_line():
    # Given
    line = OrderLine(id=0, sku="table", quantity=5)
    batch = Batch(quantity=10, reference="test", sku="table", eta=date.today())

    # When
    deallocated = batch.deallocate(line=line)

    # Then
    assert not deallocated
