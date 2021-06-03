from functools import partial


class C(partial):
    """
    Compose functions. e.g. `filter >> C(sum)`
    """

    def __rrshift__(self, other):
        return lambda *args, **kwargs: self(other(*args, **kwargs))


class CC(partial):
    """
    Compose functions. e.g. `lambda x: (x + 1, x + 2) >> CC(lambda a, b: a + b)`
    """

    def __rrshift__(self, other):
        return lambda *args, **kwargs: self(*other(*args, **kwargs))
