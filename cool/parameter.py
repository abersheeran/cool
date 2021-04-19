from .pipe import FF, F


class P:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __rmatmul__(self, function):
        return F(function, *self.args, **self.kwargs)


class PP:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __rmatmul__(self, function):
        return FF(function, *self.args, **self.kwargs)
