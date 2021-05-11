from .partial import partial


class F(partial):
    """
    Python Pipe. e.g.`range(10) | F(filter, lambda x: x % 2) | F(sum)`
    """

    def __ror__(self, other):
        return self(other)


class FF(F):
    """
    Python Pipe. e.g.`("f", 10) | FF(lambda letter, num: letter * num)`
    """

    def __call__(self, args):
        return super().__call__(*args)
