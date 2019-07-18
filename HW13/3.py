"""
Реализовать дескриптор валидации для атрибута email. Ваш дескриптор должен проверять формат email который вы пытаетесь назначить.
class EmailDescriptor:
	def __get__(self, instance, owner):
    	    # your code here
    	    pass
	def __set__(self, instance, value):
    	    # your code here
    	    pass
class MyClass:
    email = EmailDescriptor()
my_class = MyClass()
my_class.email = "validemail@gmail.com"
my_class.email = "novalidemail"
# Raised Exception
"""

class EmailValidDescriptor(object):
    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        if not self.isValid(value):
            raise TypeError
        instance._email = value

    def isValid(self, value:str):
        if "@" not in value:
            return False
        em = value.split("@")
        if "." not in em[1]:
            return False
        return True

class User(object):
    email = EmailValidDescriptor()

if __name__ == "__main__":
    u = User()
    try:
        u.email = input("email: ")
        print("good email")
    except TypeError:
        print("not valid email")