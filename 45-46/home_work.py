class Shop:
    PRODUCTS = {'молоко': 10, 'колбаса': 20}
    DISCOUNT_PRICE = {'молоко': 5}

    def __init__(self):
        self.count = 0
        self.all_sum = 0
    def buy(self, name):
        """Покупка продуктов"""
        name = name.lower()
        if name in self.PRODUCTS:
            if self._check_discount(name):
                self.all_sum += self.PRODUCTS[name] - self.DISCOUNT_PRICE[name]
                self.count += 1
                print(f'Купили {name}, скидка {self.DISCOUNT_PRICE[name]} руб.')

            else:
                self.all_sum += self.PRODUCTS[name]
                self.count += 1
                print(f'Купили {name}, скидки на этот товар нет')
        else:
            print('ТАКОГО НЕТ БЛИН')

    def add_product(self, name, price):
        """Добавляем продукт в базу"""
        self.PRODUCTS[name] = price
        print('обновили базу')
    def _check_discount(self, name):
        """Проверяем наличие скидки на товар"""
        return name in self.DISCOUNT_PRICE

    def delete_product(self, name):
        """Удаляем товар из базы данных"""
        if name in self.PRODUCTS:
            print(f'удалили {name}')
            del self.PRODUCTS[name]

        if name in self.DISCOUNT_PRICE:
            del self.DISCOUNT_PRICE[name]
    def get_info(self):
        print(f'Всего купили на {self.all_sum}р.')
        print(f'Всего чеков {self.count}')
        print('Хорошего дня!')

shop = Shop()
shop.buy('молоко')
shop.buy('Яйца')
shop.buy('Колбаса')
shop.add_product('яйца', 100)
shop.buy('яйца')
shop.delete_product('молоко')
shop.buy('молоко')
shop.get_info()