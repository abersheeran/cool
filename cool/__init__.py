from .pipe import FF, F
from .parameter import PP, P
from .redirect import R


def set_global(*args):
    import builtins

    list(args | F(map, lambda arg: setattr(builtins, arg.__name__, arg)))


__all__ = ["F", "FF", "PP", "P", "R"]
