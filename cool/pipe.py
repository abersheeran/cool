from .partial import partial


class F(partial):
    """
    Python Pipe. e.g.`range(10) | F(filter, lambda x: x % 2) | F(sum)`
    """

    def __ror__(self, other):
        return self(other)


class FF(partial):
    """
    Python Pipe. e.g.`("f", 10) | FF(lambda letter, num: letter * num)`
    """

    def __ror__(self, other):
        return self(*other)
