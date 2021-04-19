from cool import PP, P, F


def test_p():
    assert range(10) | filter @ P(lambda x: x % 2) | sum @ P() == 25
    assert (1, 2, 3) | sum @ P() == 6

    assert range(10) | map @ P(F(pow, ..., 2)) | sum @ P() == 285


def test_pp():
    assert (1, 2) | (lambda x, y: x + y) @ PP() == 3
    assert [1, 2, 3] | (lambda x, y, z: x + y + z) @ PP() == 6
