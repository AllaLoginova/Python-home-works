from random import randint

class Car:
    def __init__(self, color, fuel_quantity, fuel_use_100_km, mileage=0):
        self.color = color
        self.fuel_quantity = fuel_quantity # количество топлива -> 100
        self.fuel_use_100_km = fuel_use_100_km # расход на 100 км -> 7
        self.mileage = mileage # пробег

    def drive(self, km):
        fuel_amount_to_drive = km / 100 * self.fuel_use_100_km
        if fuel_amount_to_drive > 0 and self.fuel_quantity - fuel_amount_to_drive >= 0:
            self.fuel_quantity -= fuel_amount_to_drive
            self.mileage += km
            print(f"Мы проехали {km} км")

        else:
            print(f"Не хватает топлива")

    def get_mileage(self):
        return self.mileage
    
class SportCar(Car):
    def fast_drive(self, km):
        fuel_amount_to_drive = km / 100 * self.fuel_use_100_km * 1.5
        if fuel_amount_to_drive > 0 and self.fuel_quantity - fuel_amount_to_drive >= 0:
            self.fuel_quantity -= fuel_amount_to_drive
            self.mileage += km
            print(f"Мы проехали {km} км")

        else:
            print(f"Не хватает топлива")

    def competition(self):
        choice = randint(0, 1)
        
        if choice == 0:
            return 'Проигрыш'
        else:
            return 'Выигрыш'


car1 = Car(color='черный', fuel_quantity=8, fuel_use_100_km=8,mileage=0)
car2 = SportCar(color='черный', fuel_quantity=8, fuel_use_100_km=8, mileage=0)
print('Первая машина')
for i in range(4):
    car1.drive(30)
print('Вторая машина')
for i in range(4):
    car2.fast_drive(30)
print(car2.competition())