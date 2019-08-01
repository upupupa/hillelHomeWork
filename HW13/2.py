"""
Создать свой тип с помощью type.
"""

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

if __name__ == "__main__":
    CalClass = type(
        "CalClass",
        (object, ),
        {"addition":addition, "subtraction":subtraction, 
        "divide":divide, "multiply":multiply})
    print(CalClass)
    print(CalClass.addition(1, 2))
    print(CalClass.subtraction(1, 2))
    try:
        print(CalClass.divide(1, 0))
    except ZeroDivisionError as e:
        print(e)
    print(CalClass.multiply(2, 2))