#!/usr/bin/python
import threading
import time
import subprocess
import os
import getpass
import requests
import json

'''
@punzoamh
*This code is a basic security measure that be used to prevent unauthorized access
*to a personal PC. Set your Username and Password in the variables named accordingly 
*below. The code includes functions for getting general GPS location of system.
*A simple change can allow for these to be sent to an email address.
*Using PyInstaller a stand-alone code application can be created.
*On Windows this stand-alone application and 
*this code (extra_security.py) + IP_Location.py can be put in Start > All Programs
*This will cause the program to run automatically when computer is logged onto.
'''



global Flag
Flag = False


def ask():
    Flag = False
    i = 0
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('++                                              ++')
    print('++  Please Enter Secondary Password:            ++'
           + '\n++  You have 30 Seconds and 2 Attmepts:         ++'
           +'\n++  Failed Attempts will Result in Shut Down    ++')
    print('++                                              ++')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')


    Username = input("Username: ",)
    Password = getpass.getpass()
    while i < 1:

        if Username == 'Your User Name Here' and Password == 'Your Password Here':
            time.sleep(1)
            print('Login Successful!')
            logged()
            Flag = True
            i = 1
        else:

            print('INCORRECT')
            Username = input("Enter Username: ",)
            Password = getpass.getpass()
            i+=1
    if Flag != True:
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        print('========================================================================')
        print('========================================================================')
        print(lat)
        print(lon)
        print('=== !!! FAILURE TO ENTER THE CORRECT CREDENTIALS !!!                 ===')
        print('=== !!! THIS UNIT WILL SHUT DOWN IN 10 SECONDS !!!                   ===')
        print('=== !!! THE GPS COORDINATES OF THIS UNIT HAVE BEEN REPORTED !!!      ===')
        print('=== !!! CURRENT LATITUDE: {} CURRENT LONGITUDE: {} !!!    ==='.format(lat,lon))
        print('========================================================================')
        print('========================================================================')
        t=10
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins,secs)
            print(timeformat, end='\r', )
            time.sleep(1)
            t-=1
        subprocess.call(["shutdown", "/l"]) #log off
        exit('')
        subprocess.call(["shutdown", "/s"]) #shutdown
    time.sleep(5)
    exit('')



def exit(msg):
    print(msg)
    os._exit(1)

def message(mes):
    print(mes)

def close_if_time_pass(seconds):
    #print(threading.currentThread().getName())
    while Flag == False:
        time.sleep(seconds)
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        print('')
        print('========================================================================')
        print(lat)
        print(lon)
        print('=== !!! TIME HAS EXPIRED SHUTTING DOWN !!!                           ===')
        print('=== !!! THE GPS COORDINATES OF THIS UNIT HAVE BEEN REPORTED !!!      ===')
        print('=== !!! CURRENT LATITUDE: {} CURRENT LONGITUDE: {} !!!    ==='.format(lat,lon))
        print('========================================================================')

        time.sleep(2)
        subprocess.call(["shutdown", "/l"]) #log off
        exit("")
    """
    t=10
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,'Enter Username: ', end='\r', )
        time.sleep(1)
        t-=1
    """



def logged():
    Flag = True
    time.sleep(1)
    print('Login Successful')


def main():
    t = threading.Thread(target=close_if_time_pass, args=(20,))
    w= threading.Thread(target=ask)
    #t.setDaemon(True)


    t.start()
    w.start()
    #w.start()
    #w.join()
    #close_if_time_pass(1)


    #ask()


if __name__=="__main__":
    main()
