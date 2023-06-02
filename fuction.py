def pythagoras(*, a=None, b=None, c=None):
    """ Computes a side of a right triangle """

    # Validate
    if len([i for i in (a, b, c) if i is None or i <= 0]) != 1:
        raise SystemExit("ERROR: you need to define any of two non-negative variables")

    # Compute
    if a is None:
        return (c ** 2 - b ** 2) ** 0.5
    elif b is None:
        return (c ** 2 - a ** 2) ** 0.5
    else:
        return (a ** 2 + b ** 2) ** 0.5
