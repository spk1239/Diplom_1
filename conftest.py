import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def burgerme():
    return Burger()

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "normal bun"
    mock_bun.get_price.return_value = 1.5
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "cheese"
    mock_ingredient.get_price.return_value = 1.5
    mock_ingredient.get_type.return_value = 'FILLING'
    return mock_ingredient

@pytest.fixture
def mock_ingredient_tomato():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "tomato"
    mock_ingredient.get_price.return_value = 0.3
    mock_ingredient.get_type.return_value = 'FILLING'
    return mock_ingredient

@pytest.fixture
def mock_ingredient_beef():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "beef"
    mock_ingredient.get_price.return_value = 3.0
    mock_ingredient.get_type.return_value = 'FILLING'
    return mock_ingredient

@pytest.fixture
def mock_white_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "white bun"
    mock_bun.get_price.return_value = 1.0
    return mock_bun