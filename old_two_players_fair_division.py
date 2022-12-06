"""
All these algorithms are based on the paper: Two-player fair division of indivisible items: Comparison of algorithms
By: D. Marc Kilgour, Rudolf Vetschera

programmers: Itay Hasidi & Amichai Bitan
"""
from utils_two_players_fair_division import *
import fairpy
import operator

# divide = fairpy.divide
valuations = {"Alice": {"w": 11, "x": 22, "y": 44, "z": 0}, "George": {"w": 22, "x": 11, "y": 66, "z": 33}}


def h_m_l(u: list, h: list, l: int):
    """
    Returns all the desired items until a rank of l for a given valuations list of a player.
    """
    out_h = []
    if l < len(h):
        for i in range(l):
            # print(h[i][0])
            if h[i] in u:
                out_h.append(h[i])
    return out_h


def allocate(u_copy: list, z_copy: dict, i: any, j: any):
    """
    Allocates i to player A and j to player B. removing items i and j from all available lists.
    """
    # print(h['a'][i])
    # h['a'].pop(h['a'].index(i))
    # h['a'].pop(h['a'].index(j))
    # h['b'].pop(h['b'].index(i))
    # h['b'].pop(h['b'].index(j))
    z_copy['a'].append(i)
    z_copy['b'].append(j)
    u_copy.pop(u_copy.index(i))
    u_copy.pop(u_copy.index(j))
    return u_copy, z_copy


"""
A: a b c d
B: b c d a
TR: A: a c, B: b d
"""


def sequential(u: list, z: dict, h: dict, l: int = 1):
    """
    a.k.a OS
    the algorithm receives:
        u - all un-allocated objects.
        z - partial allocation for player a and b.
        h - valuations given to items by player a and b.
        l - the maximum rank of items currently considered for allocation

    # >>> divide(algorithm=fairpy.items.iterated_maximum_matching, input=valuations)

    """
    if not u:
        print(z)
        return z
    # print(h.get('a'))

    h_a = h_m_l(u, h['a'], l)
    h_b = h_m_l(u, h['b'], l)
    if h_a != h_b or (len(h_a) > 1 and len(h_b) > 1):
        for i in h_a:
            for j in h_b:
                if i != j:
                    old_z = {'a': [], 'b': []}
                    for player in z:
                        for item in z[player]:
                            old_z[player].append(item)
                    # old_z.clear()
                    new_u, new_z = allocate(u.copy(), old_z, i, j)
                    l += 1
                    sequential(new_u, new_z, h, l)
                    # u = new_u
                    # z = new_z
    else:
        l += 1
        sequential(u, z, h, l)

    # pass


def restricted_simple(u: list, z: dict, h: dict, l: int = 1):
    """
    a.k.a RS
    the algorithm receives:
        u - all un-allocated objects.
        z - partial allocation for player a and b.
        h - valuations given to items by player a and b.
        l - the maximum rank of items currently considered for allocation
    """
    if not u:
        print(z)
        return z
    h_a = h_m_l(u, h['a'], l)
    h_b = h_m_l(u, h['b'], l)
    if h_a != h_b or (len(h_a) > 1 and len(h_b) > 1):
        if h_a[0] != h_b[0]:
            old_z = {'a': [], 'b': []}
            for player in z:
                for item in z[player]:
                    old_z[player].append(item)
            new_u, new_z, = allocate(u.copy(), old_z, h_a[0], h_b[0])
            l += 1
            restricted_simple(new_u, new_z, h, l)
        else:
            if len(h_a) > 1:
                old_z = {'a': [], 'b': []}
                for player in z:
                    for item in z[player]:
                        old_z[player].append(item)
                new_u, new_z, = allocate(u.copy(), old_z, h_a[1], h_b[0])
                l += 1
                restricted_simple(new_u, new_z, h, l)
            if len(h_b) > 1:
                old_z = {'a': [], 'b': []}
                for player in z:
                    for item in z[player]:
                        old_z[player].append(item)
                new_u, new_z, = allocate(u.copy(), old_z, h_a[0], h_b[1])
                l += 1
                restricted_simple(new_u, new_z, h, l)
    else:
        l += 1
        restricted_simple(u, z, h, l)
    # pass


def singles_doubles(u: list, z_a: list, z_b: list):
    """
    a.k.a SD
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.
    """
    pass


def iterated_singles_doubles(u: list, z_a: list, z_b: list):
    """
    a.k.a IS
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.
    """
    pass


def s1(u: list, z_a: list, z_b: list):
    """
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.
    """
    pass


def l1(u: list, z_a: list, z_b: list):
    """
    the algorithm receives:
        z_a - partial allocation for player a.
        z_b - partial allocation for player b.
        u - all un-allocated objects.
    """
    pass


def top_down(u: list):
    """
    a.k.a TD
    u - all un-allocated objects.
    """
    pass


def top_down_alternating(u: list):
    """
    a.k.a TA
    u - all un-allocated objects.
    """
    pass


def bottom_up(u: list):
    """
    a.k.a BU
    u - all un-allocated objects.
    """
    pass


def bottom_up_alternating(u: list):
    """
    a.k.a BA
    u - all un-allocated objects.
    """
    pass


def trump(u: list):
    """
    a.k.a TR
    u - all un-allocated objects.
    """
    pass


if __name__ == '__main__':
    h = {'a': {'x': 2, 'y': 3, 'z': 4, 'w': 1}, 'b': {'x': 2, 'y': 3, 'z': 1, 'w': 4}}
    u = ['w', 'x', 'y', 'z']
    z: dict = {'a': [], 'b': []}
    pref: dict = {'a': [], 'b': []}
    h['a'] = sorted(h.get('a').items(), key=lambda x: x[1])
    h['b'] = sorted(h.get('b').items(), key=lambda x: x[1])
    h_a = []
    h_b = []
    for player in h:
        for item in h[player]:
            pref[player].append(item[0])
            if player == 'a':
                h_a.append(item[0])
            else:
                h_b.append(item[0])
    h['a'] = h_a
    h['b'] = h_b
    print("OS:")
    sequential(u, z, h)
    print("RS:")
    restricted_simple(u, z, h)
