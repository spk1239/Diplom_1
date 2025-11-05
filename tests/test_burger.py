import pytest 

class TestBurger:

    def test_set_buns(self, burgerme, mock_bun):
        burgerme.set_buns(mock_bun)
        assert burgerme.bun == mock_bun

    def test_add_ingredient(self, burgerme, mock_ingredient):
        burgerme.add_ingredient(mock_ingredient)
        assert len(burgerme.ingredients) == 1
        assert burgerme.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burgerme, mock_ingredient, mock_ingredient_tomato):
        burgerme.add_ingredient(mock_ingredient)
        burgerme.add_ingredient(mock_ingredient_tomato)
        burgerme.remove_ingredient(0)
        assert len(burgerme.ingredients) == 1
        assert burgerme.ingredients[0] == mock_ingredient_tomato

    def test_move_ingredient(self, burgerme, mock_ingredient, mock_ingredient_tomato):
        burgerme.add_ingredient(mock_ingredient)
        burgerme.add_ingredient(mock_ingredient_tomato)
        burgerme.move_ingredient(0, 1)
        assert burgerme.ingredients[0] == mock_ingredient_tomato
        assert burgerme.ingredients[1] == mock_ingredient

    def test_get_price_with_bun_and_ingredients(self, burgerme, mock_bun, mock_ingredient, mock_ingredient_tomato):
        burgerme.set_buns(mock_bun)
        burgerme.add_ingredient(mock_ingredient)
        burgerme.add_ingredient(mock_ingredient_tomato)
        price = burgerme.get_price()
        expected_price = (1.5 * 2) + 1.5 + 0.3  # 2 булки + ингредиенты
        assert price == expected_price

    def test_get_receipt(self, burgerme, mock_white_bun, mock_ingredient, mock_ingredient_beef):
        burgerme.set_buns(mock_white_bun)
        burgerme.add_ingredient(mock_ingredient)
        burgerme.add_ingredient(mock_ingredient_beef)
        receipt = burgerme.get_receipt()
        expected_receipt = (
            "(==== white bun ====)\n"
            "= filling cheese =\n"
            "= filling beef =\n"
            "(==== white bun ====)\n\n"
            "Price: 6.5"
        )
        assert receipt == expected_receipt