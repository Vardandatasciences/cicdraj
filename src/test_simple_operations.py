# test_simple_operations.py

import pytest
from simple_operations import add, multiply

# Test the add function
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

# Test the multiply function
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
