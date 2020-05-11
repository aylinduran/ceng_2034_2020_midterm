#!/usr/bin/python3
import os
import sys
import urllib.request
import threading
from multiprocessing import pool

Cpucount = (os.cpu_count())
Loadavg = (os.getloadavg())


def PrintPID():
    print("Your PID is  ", os.getpid())


PrintPID()


def LoadAvg():
    print("My operating system is ", sys.platform)
    print("MY loadavg is ", os.getloadavg())


LoadAvg()


def Calculate():
    print("Cpu core count is ", Cpucount)
    print("5 min loadavg is ", Loadavg[1])
    a = float(Cpucount - Loadavg[1])
    if a < 1:
        print(sys.exit())
    else:
        print("Your cpu core count - 5min load avg > 1 ")


Calculate()

site = ["https://api.github.com", "http://bilgisayar.mu.edu.tr/", "https://www.python.org/",
        "http://akrepnalan.com/ceng2034", "https://github.com/caesarsalad/wow"]


def check(url):
    for i in range(5):
        print("Checking...", url[i], os.getpid())
        if (urllib.request.urlopen(url[i]).getcode() == 200):
            print(url[i], " is valid")

        else:
            print("There is a error , ", url[i], " is not valid !")


check(site)

'''
thread1=threading.Thread(target=check, args=("https://www.python.org/" ,))
thread2=threading.Thread(target=check, args=("http://bilgisayar.mu.edu.tr/",))
thread3=threading.Thread(target=check, args=("https://api.github.com ",))
thread4=threading.Thread(target=check, args=("http://akrepnalan.com/ceng2034",))
thread5=threading.Thread(target=check, args=("github.com/caesarsalad/wow" ,))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join() 
thread2.join()
thread3.join()
thread4.join() 
thread5.join()
print('the endd')

  with Pool(5) as p:
    print(p.map(check, ["https://api.github.com", "http://bilgisayar.mu.edu.tr/", "https://www.python.org/",
        "http://akrepnalan.com/ceng2034", "https://github.com/caesarsalad/wow"])) '''



