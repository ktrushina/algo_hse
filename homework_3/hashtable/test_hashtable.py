import pytest
from hash_table import HashTable


def test_set_and_get():
    table = HashTable()
    table["apple"] = 10
    assert table["apple"] == 10


def test_update_existing_key():
    table = HashTable()
    table["apple"] = 10
    table["apple"] = 20
    assert table["apple"] == 20
    assert len(table) == 1


def test_get_missing_key_raises_keyerror():
    table = HashTable()
    with pytest.raises(KeyError):
        table["missing"]


def test_delete_key():
    table = HashTable()
    table["apple"] = 10
    del table["apple"]
    assert "apple" not in table
    assert len(table) == 0


def test_invalid_capacity_raises():
    with pytest.raises(ValueError):
        HashTable(capacity=0)
