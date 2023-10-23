import pytest
from vector import Vector

def test_equality():
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    v3 = Vector(4, 5, 6)

    assert v1 == v2
    assert v1 != v3

def test_addition_and_subtraction():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    result_add = v1 + v2
    result_sub = v2 - v1

    assert result_add == Vector(5, 7, 9)
    assert result_sub == Vector(3, 3, 3)

def test_scalar_multiplication():
    v1 = Vector(1, 2, 3)
    result = v1 * 2

    assert result == Vector(2, 4, 6)

def test_length():
    v1 = Vector(1, 2, 3)
    assert len(v1) == 3

def test_integer_part_of_length():
    v1 = Vector(1, 2, 3)
    assert int(v1) == 3

def test_negation():
    v1 = Vector(1, 2, 3)
    result = -v1

    assert result == Vector(-1, -2, -3)

def test_get_and_set_item():
    v1 = Vector(1, 2, 3)
    assert v1[1] == 1
    assert v1[2] == 2
    assert v1[3] == 3

    v1[1] = 4
    v1[2] = 5
    v1[3] = 6
    assert v1 == Vector(4, 5, 6)

def test_contains():
    v1 = Vector(1, 2, 3)
    assert 2 in v1
    assert 4 not in v1

def test_bool():
    v1 = Vector(1, 2, 3)
    v2 = Vector(0, 0, 0)

    assert bool(v1) is True
    assert bool(v2) is False

def test_call():
    v1 = Vector(1, 2, 3)
    v1(2)
    assert v1 == Vector(2, 4, 6)
