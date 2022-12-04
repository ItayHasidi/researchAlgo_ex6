from algorithms import *

h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 4, 'c': 2, 'd': 3, 'b': 1}}
u = ['a', 'b', 'c', 'd']
z: dict = {'a': [], 'b': []}

"""
A: a b c d
B: b c d a
"""
def test_sequential():
    assert sequential(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'c'], 'b': ['b', 'd']}, {'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_restricted_simple():
    assert restricted_simple(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}, {'a': ['a', 'c'], 'b': ['b', 'd']}]"


def test_singles_doubles():
    assert singles_doubles(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_iterated_singles_doubles():
    assert iterated_singles_doubles(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_s1():
    assert s1(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_l1():
    assert l1(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_top_down():
    assert top_down(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_top_down_alternating():
    assert top_down_alternating(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_bottom_up():
    assert bottom_up(u.copy(), z.copy(), h.copy(), to_sort=True) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_bottom_up_alternating():
    assert bottom_up_alternating(u.copy(), z.copy(), h.copy(), to_sort=True) == \
        "[{'a': ['a', 'b'], 'b': ['d', 'c']}]"


def test_trump():
    assert trump(u.copy(), z.copy(), h.copy(), to_sort=True) == \
        "[{'a': ['a', 'c'], 'b': ['b', 'd']}]"

