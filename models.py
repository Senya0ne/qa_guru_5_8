from dataclasses import dataclass, field


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity: int) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity = quantity
            return self.quantity
        else:
            raise ValueError("Продуктов не хватает!")

    def __hash__(self) -> int:
        """Метод принимает строку 'value' и возвращает целочисленный хеш-код"""
        return hash(self.name + self.description)


@dataclass
class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int] = field(default_factory=dict)

    def add_product(self, product: Product, buy_count: int = 1) -> None:
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count: int = None) -> None:
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self) -> None:
        """Метод очищает корзину покупок"""
        self.products.clear()

    def get_total_price(self) -> float:
        """Метод возвращает сумму за все товары в корзине"""
        return sum(product.price * quantity for product, quantity in self.products.items())

    def buy(self) -> None:
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        if not self.products:
            raise ValueError("Отсутствуют товары в корзине!")
        for product, quantity in self.products.items():
            if not product.check_quantity(quantity):
                raise ValueError(f"Недостаточное количество {product.name} на складе!")
        for product, quantity in self.products.items():
            product.quantity -= quantity
        self.clear()
