#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
1. Реализовать иерархию классов геометрических фигур. Базовый класс должен обязывать потомков реализовать методы - периметр и площадь. Потомки:
Треугольник
конструктор: принимает список сторон и проверяет, что в списке сторон ровно 3
    периметр
        площадь

Прямоугольник:
все аналогично треугольнику, только 2 стороны
Круг:
        принимает радиус

1* (Не обязательно). Для тех кому скучно:
Реализовать класс Point:
    атрибуты: x, y
    методы: расстояние между двумя точками, площадь под отрезком #??????????????????????

Реализовать класс Polygon:
    атрибуты: список вершин в порядке обхода по часовой стрелке
    методы: вычислить периметр, вычислить площадь
"""
from abc import ABC, abstractmethod
import math
import functools

class FigureMixin(ABC):
    def perimeter(self):
        return sum(self.sides)
    
    @abstractmethod
    def square(self):
        pass

class Triangle(FigureMixin):
    def __init__(self, *sides):
        if len(sides) != 3:
            print("must be 3 sides for triangle")
            raise OverflowError
        if not self.isTriangleExist(sides):
            print("not valid sides")
            raise Exception
        self.sides = sides
    
    def isTriangleExist(self, sides):
        if 0 not in sides:
            a, b, c = sides
            if a > 0 and b > 0 and c >0:    
                if a+b>c and a+c>b and b+c>a:
                    return True
        return False
        
    def square(self):
        hp = float(super().perimeter() / 2)
        a, b, c = self.sides
        square = float(math.sqrt(hp*(hp-a)*(hp-b)*(hp-c)))
        return square

class Rectangle(FigureMixin):
    def __init__(self, *sides):
        if len(sides) != 4:
            print("must be 4 sides for rectangle")
            raise OverflowError
        if not self.isRectangleExist(sides):
            print("not valid sides")
            raise Exception
        self.sides = sides

    def isRectangleExist(self, sides):
        if len(sides) == 4:
            if 0 not in sides:
                a, b, c, d = sides
                if a == c and b == d:
                    if a > 0 and b > 0:
                        return True
        return False
    
    def square(self):
        a = min(self.sides)
        b = max(self.sides)
        square = a*b
        return square

if __name__ == "__main__":
    t = Triangle(1, 1, 1.4)
    print(t.perimeter())
    print("%.2f" % t.square())
    r1 = Rectangle(2, 4, 2, 4)
    print(r1.perimeter())
    print(r1.square())