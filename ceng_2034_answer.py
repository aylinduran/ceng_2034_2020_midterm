#!/usr/bin/python3
import os
import os,sys
import urllib.request
import requests
import threading
import multiprocessing

from multiprocessing import pool

Cpucount=(os.cpu_count())
Loadavg=(os.getloadavg())
def PrintPID ():
   print("Your PID is  " , os.getpid())
PrintPID()

def LoadAvg ():
   print("My operating system is " , sys.platform)
   print ("MY loadavg is ", os.getloadavg())
LoadAvg()

def Calculate ():
   print("Cpu core count is " , Cpucount)
   print("5 min loadavg is " , Loadavg[1])
   a=float(Cpucount-Loadavg[1])
   if a<1:
       print(sys.exit())
   else :
       print("Your cpu core count - 5min load avg > 1 ")
Calculate()


def check(url):   
    isworking = requests.get(url)
    print(isworking.status_code, " " , url)

thread1=threading.Thread(target=check, args=("https://www.python.org/",))
thread2=threading.Thread(target=check, args=("http://bilgisayar.mu.edu.tr/",))
thread3=threading.Thread(target=check, args=("https://api.github.com",))
thread4=threading.Thread(target=check, args=("http://akrepnalan.com/ceng2034",))
thread5=threading.Thread(target=check, args=("https://github.com/caesarsalad/wow",))

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

