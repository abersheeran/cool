import functools

from cool import CC, C, F


def test_c():
    filter_sum = filter >> C(sum)

    assert filter_sum(lambda x: x % 2, range(10)) == 25


def test_cc():
    reduce = (
        (lambda a0, a1, a2=None: (a0, a1) if a2 is None else (a0, a2, a1))
        >> CC(functools.reduce)
    )
    assert range(10) | F(reduce, lambda x, y: x + y) == 45
    assert range(10) | F(reduce, lambda x, y: x + y, 55) == 100
