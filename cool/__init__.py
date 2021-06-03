from .compose import CC, C
from .pipe import FF, F
from .redirect import R


def set_global(*args):
    import builtins

    nonlazy_map = map >> C(list)

    args | F(nonlazy_map, lambda arg: setattr(builtins, arg.__name__, arg))


__all__ = ["F", "FF", "CC", "C", "R"]
