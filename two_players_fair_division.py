"""
All these algorithms are based on the paper: Two-player fair division of indivisible items: Comparison of algorithms
By: D. Marc Kilgour, Rudolf Vetschera

programmers: Itay Hasidi & Amichai Bitan
"""
from typing import List, Any, Dict
from fairpy.fairpy.agentlist import AgentList
from utils_two_players_fair_division import *


def sequential(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a OS
    the algorithm receives:
        u - all un-allocated objects.
        z - partial allocation for player a and b.
        h - valuations given to items by player a and b.
        l - the maximum rank of items currently considered for allocation

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(sequential([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    >>> u = ['computer', 'phone', 'tv', 'book']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(sequential(u, z, h, to_sort=True))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}
    {'a': ['tv', 'phone'], 'b': ['computer', 'book']}
    {'a': ['phone', 'book'], 'b': ['computer', 'tv']}
    """
    # if not u:
    #     print(z)
    #     return z
    # if to_sort:
    #     z, h = sort_inputs(z, h)
    #     to_sort = False
    # h_a = h_m_l(u, h['a'], l)  # TODO fix l incrementing
    # h_b = h_m_l(u, h['b'], l)
    # if h_a != h_b or (len(h_a) > 1 and len(h_b) > 1):
    #     for i in h_a:
    #         for j in h_b:
    #             if i != j:
    #                 old_z = {'a': [], 'b': []}
    #                 for player in z:
    #                     for item in z[player]:
    #                         old_z[player].append(item)
    #                 # old_z.clear()
    #                 new_u, new_z = allocate(u.copy(), old_z, i, j)
    #                 l += 1
    #                 sequential(new_u, new_z, h, l)
    #                 # u = new_u
    #                 # z = new_z
    # else:
    #     l += 1
    #     sequential(u, z, h, l)
    pass


def restricted_simple(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a RS
    the algorithm receives:
        u - all un-allocated objects.
        z - partial allocation for player a and b.
        h - valuations given to items by player a and b.
        l - the maximum rank of items currently considered for allocation

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(restricted_simple([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}

    >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    >>> u = ['computer', 'phone', 'tv', 'book']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(restricted_simple(u, z, h, to_sort=True))
    {'a': ['tv', 'phone'], 'b': ['computer', 'book']}
    {'a': ['phone', 'book'], 'b': ['computer', 'tv']}
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}
    """
    # if not u:
    #     print(z)
    #     return z
    # if to_sort:
    #     z, h = sort_inputs(z, h)
    #     to_sort = False
    # h_a = h_m_l(u, h['a'], l)
    # h_b = h_m_l(u, h['b'], l)
    # if h_a != h_b or (len(h_a) > 1 and len(h_b) > 1):
    #     if h_a[0] != h_b[0]:
    #         old_z = {'a': [], 'b': []}
    #         for player in z:
    #             for item in z[player]:
    #                 old_z[player].append(item)
    #         new_u, new_z, = allocate(u.copy(), old_z, h_a[0], h_b[0])
    #         l += 1
    #         restricted_simple(new_u, new_z, h, l)
    #     else:
    #         if len(h_a) > 1:
    #             old_z = {'a': [], 'b': []}
    #             for player in z:
    #                 for item in z[player]:
    #                     old_z[player].append(item)
    #             new_u, new_z, = allocate(u.copy(), old_z, h_a[1], h_b[0])
    #             l += 1
    #             restricted_simple(new_u, new_z, h, l)
    #         if len(h_b) > 1:
    #             old_z = {'a': [], 'b': []}
    #             for player in z:
    #                 for item in z[player]:
    #                     old_z[player].append(item)
    #             new_u, new_z, = allocate(u.copy(), old_z, h_a[0], h_b[1])
    #             l += 1
    #             restricted_simple(new_u, new_z, h, l)
    # else:
    #     l += 1
    #     restricted_simple(u, z, h, l)
    pass


def singles_doubles(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a SD
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(singles_doubles([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(singles_doubles(u, z, h, to_sort=True))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    >>> u = ['a', 'b', 'c', 'd']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(singles_doubles(u, z, h, to_sort=True))
    {'a': [], 'b': []}
    """
    pass


def iterated_singles_doubles(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a IS
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(iterated_singles_doubles([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(iterated_singles_doubles(u, z, h, to_sort=True))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    >>> u = ['a', 'b', 'c', 'd']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(iterated_singles_doubles(u, z, h, to_sort=True))
    {'a': [], 'b': []}
    """
    pass


def s1(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(s1([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(s1(u, z, h, to_sort=True))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    >>> u = ['a', 'b', 'c', 'd']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(s1(u, z, h, to_sort=True))
    {'a': ['b', 'd'], 'b': ['a', 'c']}
    """
    pass


def l1(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(l1([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}, 'b': {'a': 2, 'b': 4, 'c': 1, 'd': 3, 'e': 6, 'f': 5}}
    >>> u = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(l1(u, z, h, to_sort=True))
    {'a': ['a', 'b', 'e], 'b': ['c', 'd', 'f']}

    >>> h = {'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'b': {'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    >>> u = ['a', 'b', 'c', 'd']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(l1(u, z, h, to_sort=True))
    {'a': ['b', 'd'], 'b': ['a', 'c']}
    """
    pass


def top_down(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a TD
    u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(top_down([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}

    >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    >>> u = ['computer', 'phone', 'tv', 'book']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(top_down(u, z, h, to_sort=True))
    {'a': ['computer', 'tv'], 'b': ['phone', 'book']}
    """
    pass


def top_down_alternating(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a TA
    u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(top_down_alternating([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}

    >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    >>> u = ['computer', 'phone', 'tv', 'book']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(top_down_alternating(u, z, h, to_sort=True))
    {'a': ['computer', 'book'], 'b': ['phone', 'tv']}
    """
    pass


def bottom_up(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a BU
    u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(bottom_up([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'phone'], 'b': ['book', 'tv']}

    >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    >>> u = ['computer', 'phone', 'tv', 'book']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(bottom_up(u, z, h, to_sort=True))
    {'a': ['tv', 'computer'], 'b': ['phone', 'tv']}
    """
    pass


def bottom_up_alternating(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a BA
    u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(bottom_up_alternating([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    >>> u = ['computer', 'phone', 'tv', 'book']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(bottom_up_alternating(u, z, h, to_sort=True))
    {'a': ['tv', 'phone'], 'b': ['book', 'computer']}
    """
    pass


def trump(agents: AgentList, items: List[Any] = None) -> Dict:
    """
    a.k.a TR
    u - all un-allocated objects.

    >>> Alice = fairpy.agents.AdditiveAgent({'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, name = 'Alice')
    >>> George = fairpy.agents.AdditiveAgent({'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}, name = 'George')
    >>> print(trump([Alice, George], ['computer', 'phone', 'tv', 'book']))
    {'a': ['computer', 'tv'], 'b': ['book', 'phone']}

    >>> h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    >>> u = ['computer', 'phone', 'tv', 'book']
    >>> z: dict = {'a': [], 'b': []}
    >>> print(trump(u, z, h, to_sort=True))
    {'a': [], 'b': []}
    """
    pass


if __name__ == '__main__':
    # h = {'a': {'x': 2, 'y': 3, 'z': 4, 'w': 1}, 'b': {'x': 2, 'y': 3, 'z': 1, 'w': 4}}
    # u = ['w', 'x', 'y', 'z']
    # h = {'a': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}, 'b': {'computer': 4, 'phone': 2, 'tv': 3, 'book': 1}}
    h = {'a': {'computer': 1, 'phone': 3, 'tv': 2, 'book': 4}, 'b': {'computer': 1, 'phone': 2, 'tv': 3, 'book': 4}}
    u = ['computer', 'phone', 'tv', 'book']
    z: dict = {'a': [], 'b': []}

    print("OS:")
    sequential(u.copy(), z.copy(), h.copy(), to_sort=True)
    print("RS:")
    restricted_simple(u.copy(), z.copy(), h.copy(), to_sort=True)
