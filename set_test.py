from set import Set
import pytest


# add(element)

def test_add_new_element():
    set = Set()
    set.add(1)
    assert set == Set([1])


def test_add_existing_element():
    set = Set([1])
    set.add(1)
    assert set == Set([1])


# get_index(element)

def test_get_index_of_existing_element():
    set = Set([1])
    assert set.get_index(1) == 0


def test_get_index_of_non_existing_element():
    with pytest.raises(ValueError):
        set = Set([1])
        assert set.get_index(2) == 0


# remove(index)

def test_remove_existing_element_by_index():
    set = Set([1, 2, 3])
    set.remove(1)
    assert set == Set([1, 3])


def test_remove_non_existing_element_by_index():
    with pytest.raises(IndexError):
        set = Set([1, 2, 3])
        set.remove(3)
        assert set == Set([1, 2, 3])


# symmetric_difference(set)

def test_symmetric_difference_between_totally_different_sets():
    set1 = Set([1, 2, 3])
    set2 = Set([4, 5, 6])
    set3 = set1.symmetric_difference(set2)
    assert set3 == Set([1, 2, 3, 4, 5, 6])


def test_symmetric_difference_between_different_sets():
    set1 = Set([1, 2, 3, 4])
    set2 = Set([4, 5, 6, 1])
    set3 = set1.symmetric_difference(set2)
    assert set3 == Set([2, 3, 5, 6])


def test_symmetric_difference_between_totally_identical_sets():
    set1 = Set([1, 2, 3, 4])
    set2 = Set([1, 2, 3, 4])
    set3 = set1.symmetric_difference(set2)
    assert set3 == Set([])


def test_symmetric_difference_between_empty_and_non_empty_sets():
    set1 = Set([])
    set2 = Set([1, 2, 3, 4])
    set3 = set1.symmetric_difference(set2)
    assert set3 == Set([1, 2, 3, 4])


def test_symmetric_difference_between_both_empty_sets():
    set1 = Set([])
    set2 = Set([])
    set3 = set1.symmetric_difference(set2)
    assert set3 == Set([])
