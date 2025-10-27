import pytest

from praktikum.burger import Burger

@pytest.fixture
def burgerme():
    return Burger()