
def h_m_l(u: list, h: list, l: int):
    """
    Returns all the desired items until a rank of l for a given valuations list of a player.
    """
    out_h = []
    if l <= len(h):
        for i in range(l):
            if h[i] in u:
                out_h.append(h[i])
    return out_h


def allocate(u_copy: list, z_copy: dict, i: any, j: any):
    """
    Allocates i to player A and j to player B. removing items i and j from all available lists.
    """
    z_copy['a'].append(i)
    z_copy['b'].append(j)
    u_copy.pop(u_copy.index(i))
    u_copy.pop(u_copy.index(j))
    return u_copy, z_copy


def sort_inputs(z: dict, h: dict):
    """
    Sorts the valuations list for each player in ascending order.
    """
    pref: dict = {'a': [], 'b': []}
    h['a'] = sorted(h.get('a').items(), key=lambda x: x[1])
    h['b'] = sorted(h.get('b').items(), key=lambda x: x[1])
    for player in h:
        for item in h[player]:
            pref[player].append(item[0])
    h = pref
    return z, h
