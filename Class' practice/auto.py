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
        # self._v_engine = None
        # self._mileage = None
        # self._color = None
        # self._max_speed = None
        # self._max_fuel = None
        # self._price = None

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

    # @classmethod
    # def sort(cls, other):
    #     if cls.price == other.price:
    #         if cls.v_engine == other.v_engine:
    #             if cls._max_fuel == other.max_fuel:
    #                 return False
    #             elif cls.max_fuel < other.max_fuel:
    #                 return True
    #         elif cls.v_engine < other.v_engine:
    #             return True
    #     if cls.price < other.price:
    #         return True
    #     return False
    
    # @property
    # def v_engine(self):
    #     return self._v_engine
    # @v_engine.setter
    # def v_engine(self, value):
    #     self._v_engine = value
    
    # @property
    # def mileage(self):
    #     return self._mileage
    # @mileage.setterred
    # def mileage(selred
    #     self._mileared

    # @property
    # def color(self):
    #     return self._color
    # @color.setter
    # def color(self, value):
    #     self._color = value

    # @property
    # def max_speed(self):
    #     return self._max_speed
    # @max_speed.setter
    # def max_speed(self, value):
    #     self._max_speed = valuered
    
    # @property
    # def max_fuel(self):
    #     return self._max_fuel
    # @max_fuel.setter
    # def max_fuel(self, value):
    #     self._max_fuel = value
    
    # @property
    # def price(self):
    #     return self._price
    # @price.setter
    # def price(self, value):
    #     self._price = value

if __name__ == "__main__":
    auto0 = Auto(2.0, 130000, "black", 260, 60, 4000)
    auto1 = Auto(1.6, 80000, "blue", 190, 55, 3600)
    auto2 = Auto(1.8, 1200, "red", 240, 60, 1000)
    auto3 = Auto(2.0, 15000, "gray", 200, 50, 4000)
    # auto0.v_engine, auto0.mileage, auto0.color, auto0.max_speed, auto0.max_fuel, auto0.price = (2.0, 130000, "black", 260, 60, 4000)
    # auto1.v_engine, auto1.mileage, auto1.color, auto1.max_speed, auto1.max_fuel, auto1.price = (1.6, 80000, "blue", 190, 55, 3600)
    # auto2.v_engine, auto2.mileage, auto2.color, auto2.max_speed, auto2.max_fuel, auto2.price = (1.8, 1200, "red", 240, 60, 1000)
    # auto3.v_engine, auto3.mileage, auto3.color, auto3.max_speed, auto3.max_fuel, auto3.price = (2.0, 15000, "gray", 200, 60, 4000)
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