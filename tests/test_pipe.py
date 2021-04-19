import functools

from cool import FF, F, set_global

set_global(functools.reduce)


def test_f():
    assert range(10) | F(filter, lambda x: x % 2) | F(sum) == 25
    assert (1, 2, 3) | F(sum) == 6

    assert range(10) | F(reduce, lambda x, y: x + y) == 45
    assert range(10) | F(reduce, lambda x, y: x + y, ..., 10) == 55

    assert range(10) | F(map, F(pow, ..., 2)) | F(sum) == 285


def test_ff():
    assert (1, 2) | FF(lambda x, y: x + y) == 3
    assert [1, 2, 3] | FF(lambda x, y, z: x + y + z) == 6
