from algorithms import *
from two_players_fair_division import *
from typing import List, Any, Dict
from fairpy.fairpy.agentlist import AgentList

h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 4, 'c': 2, 'd': 3, 'b': 1}}
u = ['a', 'b', 'c', 'd']
z: dict = {'a': [], 'b': []}

"""
A: a b c d
B: b c d a
"""
def test_sequential():
    assert sequential(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'c'], 'b': ['b', 'd']}, {'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_restricted_simple():
    assert restricted_simple(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}, {'a': ['a', 'c'], 'b': ['b', 'd']}]"


def test_singles_doubles():
    assert singles_doubles(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_iterated_singles_doubles():
    assert iterated_singles_doubles(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_s1():
    assert s1(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_l1():
    assert l1(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_top_down():
    assert top_down(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_top_down_alternating():
    assert top_down_alternating(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_bottom_up():
    assert bottom_up(agents: AgentList, items: List[Any] = None) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_bottom_up_alternating():
    assert bottom_up_alternating(agents: AgentList, items: List[Any] = None) == \
        "[{'a': ['a', 'b'], 'b': ['d', 'c']}]"


def test_trump():
    assert trump(agents: AgentList, items: List[Any] = None) == \
        "[{'a': ['a', 'c'], 'b': ['b', 'd']}]"

