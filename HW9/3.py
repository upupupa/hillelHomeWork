#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
 Создайте класс который будет хранить параметры для подключения к физическому юниту(например switch). 
 В своем списке атрибутов он должен иметь минимальный набор (unit_name, mac_address, ip_address, login, password). 
 Вы должны описать каждый из этих атрибутов в виде гетеров и сеттеров(@property). У вас должна быть возможность 
 получения и назначения этих атрибутов в классе.
"""

class PhysUnit(object):
    def __init__(self):
        self._unit_name = None
        self._mac_address = None
        self._ip_address = None
        self._login = None
        self._password = None

    def __repr__(self):
        print(self.unit_name, self.mac_address, self.ip_address, self.login, self.password)
        return ""
    
    @property
    def unit_name(self):
        return self._unit_name
    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value

    @property
    def mac_address(self):
        return self._mac_address
    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value

    @property
    def ip_address(self):
        return self._ip_address
    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        self._login = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

if __name__ == "__main__":
    pu = PhysUnit()
    pu.unit_name = "name"
    pu.mac_address = "00:00:00:00:00"
    pu.ip_address = "127.0.0.1"
    pu.login = "admin"
    pu.password = "admin"
    print(pu)
    print(pu.unit_name, pu.mac_address)