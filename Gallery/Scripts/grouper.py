from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    """
    Grouper from more-itertools
    Group elements from iterable into n-long subgroups, and fill last values if needed with fillvalue
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)