class Car:

    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color  # Цвет
        self.consumption = consumption  # Средний расход топлива
        self.tank_volume = tank_volume  # Объём бака
        self.reserve = tank_volume  # Текущий запас топлива
        self.mileage = mileage  # Пробег
        self.engine_on = False  # Состояние двигателя

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен!"
        return "Двигатель уже был запущен!"

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель заглушен!"
        return "Двигатель уже был заглушен!"

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен!"
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива!"
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехаели {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

car_1 = Car(color="black", consumption=10, tank_volume=55)
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(500))
print(f"Пробег {car_1.get_mileage()} км.")
print(f"Запас топлива {car_1.get_reserve()} л.")
print(car_1.stop_engine())
print(car_1.drive(100))
print()
car_2 = Car(color="yellow", consumption=15, tank_volume=50)
print(car_2.start_engine())
print(car_2.drive(150))
print(car_2.drive(300))
print(f"Пробег {car_2.get_mileage()} км.")
print(f"Запас топлива {car_2.get_reserve()} л.")
print(car_2.stop_engine())
print(car_2.drive(500))