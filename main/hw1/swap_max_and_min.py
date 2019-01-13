def swap_max_and_min(vals):
    min = max = vals[0]
    if len(vals) > len(set(vals)): raise ValueError
    for i in vals:
        if (type(i) is not int): raise TypeError
        min = i if (i < min) else min
        max = i if (i > max) else max
    vals[list(vals).index(max)] = min
    vals[list(vals).index(min)] = max
    return vals
