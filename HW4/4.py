#!bin/usr/python3
# -*- encoding: utf-8 -*-

"""
4. Дан список словарей. Нужно их отсортировать. 
- по стоимости, от больших к меньшим
- использовать для сортировки лямбду и обычную функцию
autos = [
  {"brand": "Ford", "model": "Mustang", "year": 1964, "price": 4000},
  {"brand": "Ford", "model": "Mondeo", "year": 1999, "price": 3000},
  {"brand": "Ford", "model": "Fiesta", "year": 2003, "price": 4200},
  {"brand": "Nissan", "model": "Primera", "year": 1997, "price": 3100},
  {"brand": "BMW", "model": "X3", "year": 2001, "price": 5000},
  {"brand": "Nissan", "model": None, "year": 1964, "price": None},
  {"brand": "VW", "model": "Passat", "year": 1996, "price": 1200},
  {"brand": "BMW", "model": "X5", "year": 2010, "price": 7500},
  {"brand": "Renault", "model": "Megane", "year": 1999, "price": 2300}
]
"""

def bubblesort(l):
    flag = None
    for i in range(0, len(l)):
        for j in range(0, len(l)-1):
            if l[j]["price"] == None:
                continue
            if l[i]["price"] == None:
                flag = l[-1]
                l[-1] = l[i]
                l[i] = flag
            elif l[i]["price"] > l[j]["price"]:
                flag = l[j]
                l[j] = l[i]
                l[i] = flag
    return l

if __name__ == "__main__":
    autos = [
        {"brand": "Ford", "model": "Mustang", "year": 1964, "price": 4000},
        {"brand": "Ford", "model": "Mondeo", "year": 1999, "price": 3000},
        {"brand": "Ford", "model": "Fiesta", "year": 2003, "price": 4200},
        {"brand": "Nissan", "model": "Primera", "year": 1997, "price": 3100},
        {"brand": "BMW", "model": "X3", "year": 2001, "price": 5000},
        {"brand": "Nissan", "model": None, "year": 1964, "price": None},
        {"brand": "VW", "model": "Passat", "year": 1996, "price": 1200},
        {"brand": "BMW", "model": "X5", "year": 2010, "price": 7500},
        {"brand": "Renault", "model": "Megane", "year": 1999, "price": 2300}
    ]
    replicaAutos = autos[:]
    print(autos)
    print(bubblesort(replicaAutos))
    lambdasortedAutos = sorted(list(filter(lambda x: x["price"] is not None, autos)), key=lambda y: y["price"], reverse=True)
    print(lambdasortedAutos)