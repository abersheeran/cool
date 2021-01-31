from example.__version__ import VERSION, __version__  # TODO


def test_version():
    VERSION[0]
    VERSION[1]
    VERSION[2]

    assert isinstance(__version__, str)
