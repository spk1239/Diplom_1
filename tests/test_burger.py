from unittest.mock import Mock
import pytest 

class TestBurger:

    def test_set_buns(self, burgerme):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "normal bun"
        mock_bun.get_price.return_value = 1.5

        burgerme.set_buns(mock_bun)

        assert burgerme.bun == mock_bun

    def test_add_ingredient(self, burgerme):

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "cheese"
        mock_ingredient.get_price.return_value = 0.5
        mock_ingredient.get_type.return_value = 'FILLING'

        burgerme.add_ingredient(mock_ingredient)

        assert len(burgerme.ingredients) == 1
        assert burgerme.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burgerme):

        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        
        burgerme.add_ingredient(mock_ingredient1)
        burgerme.add_ingredient(mock_ingredient2)

        burgerme.remove_ingredient(0)

        assert len(burgerme.ingredients) == 1
        assert burgerme.ingredients[0] == mock_ingredient2


    def test_move_ingredient(self, burgerme):

        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "cheese"
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "tomato"
        
        burgerme.add_ingredient(mock_ingredient1)
        burgerme.add_ingredient(mock_ingredient2)

        burgerme.move_ingredient(0, 1)

        assert burgerme.ingredients[0] == mock_ingredient2
        assert burgerme.ingredients[1] == mock_ingredient1


    def test_get_price_with_bun_and_ingredients(self, burgerme):
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 2.0
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 1.5
        
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 0.8

        burgerme.set_buns(mock_bun)
        burgerme.add_ingredient(mock_ingredient1)
        burgerme.add_ingredient(mock_ingredient2)

        price = burgerme.get_price()

        expected_price = (2.0 * 2) + 1.5 + 0.8  # 2 булки + ингредиенты

        assert price == expected_price

    def test_get_receipt(self, burgerme):
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 1.0
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "cheddar"
        mock_ingredient1.get_price.return_value = 1.5
        mock_ingredient1.get_type.return_value = 'FILLING'
        
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "beef"
        mock_ingredient2.get_price.return_value = 3.0
        mock_ingredient2.get_type.return_value = 'FILLING'

        burgerme.set_buns(mock_bun)
        burgerme.add_ingredient(mock_ingredient1)
        burgerme.add_ingredient(mock_ingredient2)

        receipt = burgerme.get_receipt()


        expected_receipt = (
            "(==== white bun ====)\n"
            "= filling cheddar =\n"
            "= filling beef =\n"
            "(==== white bun ====)\n\n"
            "Price: 6.5"
        )
        assert receipt == expected_receipt