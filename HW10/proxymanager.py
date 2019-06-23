"""
V0*. ProxyManager
Реализовать классы которые будет управлять списком адресов прокси серверов. Формат адреса - ip:port. 
Читать адреса из файла.
Хранить статус (OK и BANNED) и дату последнее использование каждой прокси, а также количество раз её использования. 
Статусы можно реализовать путем хранения адресов в двух разных контейнерах.
По запросу возвращает адрес из рабочих прокси с самым старым временем использования. 
При этом в каждый момент времени один адрес может быть использован только в одном экземпляре. 
Принимает обратно использованный адрес со статусом.
Если при обращении за следующей прокси - не будет успешных - выводить сообщение что "прокси закончились".
"""
import time

class Proxy(object):
    def __init__(self, ip, port, user, pw, date_used=None, count=0):
        self.ip = ip
        self.port = port
        self.user = user
        self.pw = pw
        self.date_used = date_used
        self.count = count

    def __repr__(self):
        return "IP: {}, Port: {}, User: {}, PW: {}, Used: {}, Counter: {}".format(self.ip, self.port, self.user, self.pw, self.date_used, self.count)

class ProxyManager(object):
    def __init__(self):
        self.ok = []
        self.banned = [] #fifo - первый самый старший
    
    def next_proxy(self):
        if len(self.ok) == 0:
            print("proxy has ended")
            #get proxy from banned that been used long time ago
            print("returning the old one from banned")
            return self.banned.pop(0)
        return self.ok.pop(0)
    
    def back_poxy(self, proxy: Proxy, status:bool):
        proxy.date_used = time.time()
        if status:
            self.ok.append(proxy)
            return
        self.banned.append(proxy)
        return

    def read_from_file(self, fp):
        raw_proxy = []
        with open(fp, "r") as f:
            for line in f:
                raw_proxy.append(line.strip())
            f.close()
        for i in range(0, len(raw_proxy)):
            ip, port, user, pw = raw_proxy[i].split(" ")
            proxy = Proxy(ip, port, user, pw)
            self.ok.append(proxy)
        return

if __name__ == "__main__":
    pm = ProxyManager()
    pm.read_from_file("proxy.txt")
    for i in pm.ok:
        print(i)
    for i in range(7):
        np = pm.next_proxy()
        pm.back_poxy(np, False)
        print("OK: {}".format(pm.ok))
        print("BAN: {}".format(pm.banned))