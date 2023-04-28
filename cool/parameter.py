from .pipe import FF, F


class _PMeta(type):
    def __rmatmul__(cls, function):
        return cls._F_class(function)


class _PBase(metaclass=_PMeta):
    __slots__ = ("args", "kwargs")

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __rmatmul__(self, function):
        return self._F_class(function, *self.args, **self.kwargs)


class P(_PBase):
    _F_class = F


class PP(_PBase):
    _F_class = FF
