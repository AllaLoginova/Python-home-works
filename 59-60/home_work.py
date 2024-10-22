class Shop:
    def __init__(self):
        self.products = {'яблоко': 200, 'манго': 100}
        self.check = 0

    def buy_product(self, name):
        if name not in self.products:
            raise ValueError('такого товара нет')
        self.check += self.products[name]
        print(f'Купили товар {name}')

    def add_product(self, name, price):
        if price < 0:
            raise ValueError('цена товара не может быть отрицательной')
        elif len(name) < 3:
            raise ValueError('название товара меньше 3 букв')
        self.products.update({name: price})
        print(f'Добавили товар {name} по цене {price}')


shop = Shop()
while True:
    print('Что вы хотите сделать: ')
    print('1 - купить товар')
    print('2 - добавить товар')
    print('q - выход')

    ans = input('Выберите: ')

    if ans == '1':
        name = input('Введите название товара: ')
        try:
            shop.buy_product(name)
        except ValueError as e:
            print(e)

    elif ans == '2':
        name = input('Введите название товара: ')
        price = int(input('Введите цену товара: '))
        try:
            shop.add_product(name, price)
        except ValueError as e:
            print(e)

    elif ans == 'q':
        break