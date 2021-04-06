import sys
from contextlib import contextmanager
from functools import partial
from io import TextIOBase
from pathlib import PurePath


@contextmanager
def redirect(fd):
    _stdout = sys.stdout
    _stderr = sys.stderr

    try:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout = fd
        sys.stderr = fd
        yield None
    finally:
        fd.flush()
        fd.flush()
        sys.stdout = _stdout
        sys.stderr = _stderr


class Null(TextIOBase):
    """
    /dev/null
    """

    def write(self, text):
        return len(text)


class R(partial):
    """
    Python redirect. e.g.`R(print, "hello") > Path("filepath")`
    """

    def __gt__(self, other):
        """
        impl `>` with `w+` mode
        """
        if isinstance(other, PurePath):
            with open(other, "w+", encoding="utf8") as file:
                with redirect(file):
                    return self()

        elif isinstance(other, TextIOBase):
            if other.seekable():
                other.seek(0, 0)
            with redirect(other):
                return self()

        elif other is None:
            with redirect(Null()):
                return self()

        return NotImplemented

    def __rshift__(self, other):
        """
        impl `>>` with `a+` mode
        """
        if isinstance(other, PurePath):
            with open(other, "a+", encoding="utf8") as file:
                with redirect(file):
                    return self()

        elif isinstance(other, TextIOBase):
            if other.seekable():
                other.seek(0, 2)
            with redirect(other):
                return self()

        elif other is None:
            with redirect(Null()):
                return self()

        return NotImplemented
