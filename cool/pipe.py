from functools import partial


class F(partial):
    """
    Python Pipe. e.g.`range(10) | F(filter, lambda x: x % 2) | F(sum)`

    WARNING: There will be a small performance loss when building a
    pipeline. Please do not use it in performance-sensitive locations.
    """

    def __ror__(self, other):
        return self(other)


class FF(partial):
    """
    Python Pipe. e.g.`("f", 10) | FF(lambda letter, num: letter * num)`

    WARNING: There will be a small performance loss when building a
    pipeline. Please do not use it in performance-sensitive locations.
    """

    def __ror__(self, other):
        return self(*other)
