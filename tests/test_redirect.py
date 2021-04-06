from __future__ import print_function

import os
from io import StringIO
from pathlib import PurePath

import pytest

from cool import R


@pytest.fixture
def out():
    return StringIO("")


def print_hello():
    print("hello", end=" ")


def print_world():
    print("world")


def test_r_w(out):
    R(print_hello) > out
    out.seek(0, 0)
    assert out.read() == "hello "

    R(print_world) > out
    out.seek(0, 0)
    assert out.read() == "world\n"


def test_r_a(out):
    R(print_hello) >> out
    R(print_world) >> out
    out.seek(0, 0)
    assert out.read() == "hello world\n"


def test_r_file():
    filepath = PurePath("filepath")
    try:
        R(print_hello) > filepath
        with open(filepath, encoding="utf8") as file:
            assert file.read() == "hello "

        R(print_hello) >> filepath
        with open(filepath, encoding="utf8") as file:
            assert file.read() == "hello " * 2

        with open(filepath, "w+", encoding="utf8") as file:
            R(print_hello) > file
            file.seek(0, 0)
            assert file.read() == "hello "

            R(print_hello) >> file
            file.seek(0, 0)
            assert file.read() == "hello " * 2

    finally:
        os.remove(filepath)


def test_r_null():
    R(print_hello) > None
    R(print_hello) >> None


def test_r_error():
    with pytest.raises(TypeError):
        R(print_hello) > 0

    with pytest.raises(TypeError):
        R(print_hello) >> 0
