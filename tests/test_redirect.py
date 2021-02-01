from __future__ import print_function

import os
from io import StringIO

import pytest

from cool import R


@pytest.fixture
def out():
    return StringIO("")


def print_hello():
    print("hello")


def print_world():
    print("world")


def test_r_w(out):
    R(print_hello) > out
    out.read() == "hello"

    R(print_world) > out
    out.read() == "world"


def test_r_a(out):
    R(print_hello) >> out
    R(print_world) >> out
    out.read() == "helllworld"


def test_r_file():
    try:
        R(print_hello) > "filepath"
        with open("filepath", encoding="utf8") as file:
            assert file.read() == "hello\n"

        R(print_hello) >> "filepath"
        with open("filepath", encoding="utf8") as file:
            assert file.read() == "hello\n" * 2

        with open("filepath", "w+", encoding="utf8") as file:
            R(print_hello) > file
            file.seek(0, 0)
            assert file.read() == "hello\n"

            R(print_hello) >> file
            file.seek(0, 0)
            assert file.read() == "hello\n" * 2

    finally:
        os.remove("filepath")


def test_r_null():
    R(print_hello) > None
    R(print_hello) >> None


def test_r_error():
    with pytest.raises(TypeError):
        R(print_hello) > 0

    with pytest.raises(TypeError):
        R(print_hello) >> 0
