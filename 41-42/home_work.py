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
    
# car = Car('black', 5, 7, 10000)

# car.drive(150)
# print(f"Пробег: {car.mileage}")
