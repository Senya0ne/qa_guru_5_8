"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    @pytest.mark.parametrize("quantity", (1, 999, 1000))
    def test_product_check_quantity(self, product, quantity):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(quantity)

    # @pytest.mark.parametrize("quantity", quantity_values)
    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1000)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match='Продуктов не хватает!'):
            product.buy(quantity=10000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product):
        cart = Cart()
        cart.add_product(product)
        assert cart.products == {product: 1}

    def test_add_product_greater_than_1(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.add_product(product, 5)
        assert cart.products == {product: 15}

    def test_remove_product(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product, remove_count=1)
        assert cart.products == {product: 9}

    def test_remove_product_all(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product, remove_count=10)
        assert cart.products == {}

    def test_remove_product_all_without_remove_count(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert cart.products == {}

    def test_remove_more_products_than_there_are_in_the_cart(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        cart.remove_product(product, remove_count=20)
        assert cart.products == {}

    def test_clear_cart(self, product):
        cart = Cart()
        cart.add_product(product)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, product):
        cart = Cart()
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

    def test_buy(self, product):
        cart = Cart()
        cart.add_product(product)
        cart.buy()
        assert cart.products == {}

    def test_buy_with_empty_cart(self, product):
        cart = Cart()
        with pytest.raises(ValueError, match='Отсутствуют товары в корзине!'):
            cart.buy()
