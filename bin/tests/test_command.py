# -*- config: utf-8 -*-

from bin.command import *
import pytest

# try:
# from unitest.mock import MagicMock
# except ImportError:
#    from mock import MagicMock


def test_proxy_on():
    proxy_on()
    assert(True)


def test_proxy_off():
    proxy_off()
    assert(True)


def test_proxy_info():
    proxy_info()
    assert(True)


def test_proxy_state():
    proxy_info()
    assert(True)


def test_proxy_toggle():
    proxy_toggle()
    assert(True)
