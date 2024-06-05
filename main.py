class Car:
    price = 1000000

    def horse_powers(self):
        print(self.price)


class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        print(self.price)


class Kia(Car):
    price = 3000000

    def horse_powers(self):
        print(self.price)


car = Car()
car.horse_powers()
nissan = Nissan()
nissan.horse_powers()
kia = Kia()
kia.horse_powers()
