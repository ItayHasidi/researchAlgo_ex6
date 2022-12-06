"""
All these algorithms are based on the paper: Two-player fair division of indivisible items: Comparison of algorithms
By: D. Marc Kilgour, Rudolf Vetschera

programmers: Itay Hasidi & Amichai Bitan
"""
from typing import List, Any, Dict
from fairpy.fairpy.agentlist import AgentList


def sequential(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a OS. The algorithm returns envy-free allocations if they exist, does not return max-min allocation
    and returns one Pareto optimality allocation.
    the algorithm receives:
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test 1 :
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(sequential([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    # test 2 :
    # >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    # >>> u = ['computer', 'phone', 'tv', 'book']
    # >>> z: dict = {'a': [], 'b': []}
    # # >>> print(sequential(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'George')
    >>> print(sequential([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}
    {'a': ['tv', 'phone'], 'b': ['computer', 'book']}
    {'a': ['phone', 'book'], 'b': ['computer', 'tv']}
    """
    pass


def restricted_simple(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a RS. The algorithm does not return envy-free allocations, does not return max-min allocations
    and does not return one Pareto optimality allocations.
    the algorithm receives:
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(restricted_simple([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}

    # rest 2:
    # >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    # >>> u = ['computer', 'phone', 'tv', 'book']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(restricted_simple(u, z, h, to_sort=True))

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'George')
    >>> print(restricted_simple([Alice, George], ['computer', 'phone', 'tv', 'book']))

    {'a': ['tv', 'phone'], 'b': ['computer', 'book']}
    {'a': ['phone', 'book'], 'b': ['computer', 'tv']}
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}
    """
    pass


def singles_doubles(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a SD. The algorithm returns envy-free allocations, returns max-min allocations
    and returns one Pareto optimality allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test 1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(singles_doubles([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}
    # test 2:
    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    # >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(singles_doubles(u, z, h, to_sort=True))

    >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}, name = 'George')
    >>> print(singles_doubles([Alice, George], ['a', 'b', 'c', 'd', 'e', 'f']))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    # test 3:

    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    # >>> u = ['a', 'b', 'c', 'd']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(singles_doubles(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'George')
    >>> print(singles_doubles([Alice, George], ['a', 'b', 'c', 'd']))
    {'a': [], 'b': []}
    """
    pass


def iterated_singles_doubles(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a IS. The algorithm returns envy-free allocations, returns max-min allocations
    and returns one Pareto optimality allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.
    # test 1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(iterated_singles_doubles([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    # rest2 :
    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    # >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(iterated_singles_doubles(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}, name = 'George')
    >>> print(iterated_singles_doubles([Alice, George], ['a', 'b', 'c', 'd', 'e', 'f']))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    # test 3:
    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    # >>> u = ['a', 'b', 'c', 'd']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(iterated_singles_doubles(u, z, h, to_sort=True))
     >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'George')
    >>> print(iterated_singles_doubles([Alice, George], ['a', 'b', 'c', 'd']))
    {'a': [], 'b': []}
    """
    pass


def s1(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    The algorithm returns envy-free allocations if they exist and returns max-min allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(s1([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    # test2:

    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    # >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(s1(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}, name = 'George')
    >>> print(s1([Alice, George], ['a', 'b', 'c', 'd', 'e', 'f']))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    # test 3:

    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    # >>> u = ['a', 'b', 'c', 'd']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(s1(u, z, h, to_sort=True)
    >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'George')
    >>> print(s1([Alice, George], ['a', 'b', 'c', 'd']))
    {'a': ['b', 'd'], 'b': ['a', 'c']}
    """
    pass


def l1(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    The algorithm returns envy-free allocations if they exist and returns max-min allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(l1([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    # test2:
    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    # >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(l1(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}, name = 'George')
    >>> print(l1([Alice, George], ['a', 'b', 'c', 'd', 'e', 'f']))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    # test3:
    # >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    # >>> u = ['a', 'b', 'c', 'd']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(l1(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'George')
    >>> print(l1([Alice, George], ['a', 'b', 'c', 'd']))
    {'a': ['b', 'd'], 'b': ['a', 'c']}
    """
    pass


def top_down(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a TD. The algorithm does not return envy-free allocations and returns max-min allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(top_down([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}

    # test2:
    # >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    # >>> u = ['computer', 'phone', 'tv', 'book']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(top_down(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'George')
    >>> print(top_down([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'tv'], 'b': ['phone', 'book']}
    """
    pass


def top_down_alternating(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a TA. The algorithm does not return envy-free allocations and returns max-min allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(top_down_alternating([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}

    # test2:

    # >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    # >>> u = ['computer', 'phone', 'tv', 'book']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(top_down_alternating(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'George')
    >>> print(top_down([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}
    """
    pass


def bottom_up(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a BU. The algorithm does not return envy-free allocations and does not return max-min allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(bottom_up([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}

    # test2:
    # >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    # >>> u = ['computer', 'phone', 'tv', 'book']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(bottom_up(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'George')
    >>> print(top_down([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['tv', 'computer'], 'b': ['phone', 'tv']}
    """
    pass


def bottom_up_alternating(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a BA. The algorithm does not return envy-free allocations and does not return max-min allocations.
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(bottom_up_alternating([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    # test 2:
    # >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    # >>> u = ['computer', 'phone', 'tv', 'book']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(bottom_up_alternating(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'George')
    >>> print(top_down([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['tv', 'phone'], 'b': ['book', 'computer']}
    """
    pass


def trump(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a TR. The algorithm returns envy-free allocations, does not return max-min allocations
    and returns one Pareto optimality allocations.
    the algorithm receives:
    :param agents A list that represent the players(agents) and for each player his valuation for each item, plus the
    player's name.
    :param items A list of all existing items (U).

    # test1:
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(trump([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    # test2:
    # >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    # >>> u = ['computer', 'phone', 'tv', 'book']
    # >>> z: dict = {'a': [], 'b': []}
    # >>> print(trump(u, z, h, to_sort=True))
    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'George')
    >>> print(top_down([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': [], 'b': []}
    """
    pass


if __name__ == '__main__':
    # h = {'a': {'x': 2, 'y': 3, 'z': 4, 'w': 1}, 'b': {'x': 2, 'y': 3, 'z': 1, 'w': 4}}
    # u = ['w', 'x', 'y', 'z']
    # h = {'a': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, 'b': {'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}}
    h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    u = ['a', 'b', 'c', 'd']
    z: dict = {'a': [], 'b': []}

    print("OS:")
    sequential(u.copy(), z.copy(), h.copy(), to_sort=True)
    print("RS:")
    restricted_simple(u.copy(), z.copy(), h.copy(), to_sort=True)
