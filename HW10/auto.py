"""
Реализовать класс Автомобиль:
атрибуты:
объем двигателя,
пробег,
цвет,
максимальная скорость,
максимальный запас топлива,
цена

Создать список автомобилей
Отсортировать его в такой последовательности:
    цена
    объем двигателя
    максимальный запас топлива
(Использовать методы класса)
"""

class Auto(object):
    def __init__(self, v_engine, mileage, color, max_speed, max_fuel, price):
        self.v_engine = v_engine
        self.mileage = mileage
        self.color = color
        self.max_speed = max_speed
        self.max_fuel = max_fuel
        self.price = price

    def __le__(self, other):
        if self.price == other.price:
            if self.v_engine == other.v_engine:
                if self.max_fuel == other.max_fuel:
                    return False
                elif self.max_fuel < other.max_fuel:
                    return True
            elif self.max_fuel < other.max_fuel:
                return True
        if self.price < other.price:
            return True
        return False

    def __repr__(self):
        return "Volume: {}, Mileage: {}, Color: {}, Max speed: {}, Max fuel: {}, Price: {}".format(self.v_engine, self.mileage, self.color, self.max_speed, self.max_fuel, self.price)

if __name__ == "__main__":
    auto0 = Auto(2.0, 130000, "black", 260, 60, 4000)
    auto1 = Auto(1.6, 80000, "blue", 190, 55, 3600)
    auto2 = Auto(1.8, 1200, "red", 240, 60, 1000)
    auto3 = Auto(2.0, 15000, "gray", 200, 50, 4000)
    l = [auto0, auto1, auto2, auto3]
    for i in l:
        print(i)
    for i in range(0, len(l)):
        flag = None
        for j in range(0, len(l)-1):
            if l[i] <= (l[j]):
                flag = l[j]
                l[j] = l[i]
                l[i] = flag
    print("Sorted:")
    for i in l:
        print(i)