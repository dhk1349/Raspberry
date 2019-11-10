#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:46:02 2019

@author: donghoon
"""
import requests, json

import RPi.GPIO as GPIO

import time

parking_lot="A"
is_parked=1
parking_space="01"

temp_is_parked=-1


com_code = '1234'
params = {'parkinglot_id': parking_lot, "isparked":is_parked ,"parkingspace":parking_space}
url = 'http://119.206.253.138/api/test'
#response = requests.post(url = url, data = json.dumps(params))
#print (response.json())

usleep=lambda x: time.sleep(x/1000000.0)

import datetime as dt



TP=11
EP=10
green=[4, 18, 22, 24, 17, 27, 23, 25]
red=[6, 13, 19, 26, 12, 16, 20, 21]

def getDistance():
    fDistance = 0.0
    nStartTime, nEndTime=0,0
    
    GPIO.output(TP, GPIO.LOW)
    usleep(2)
    
    GPIO.output(TP, GPIO.HIGH)
    usleep(10)
    
    GPIO.output(TP, GPIO.LOW)
    
    while(GPIO.input(EP)==GPIO.LOW):
        pass
    nStartTime = dt.datetime.now()
    while(GPIO.input(EP)==GPIO.HIGH):
        pass
    nEndTime = dt.datetime.now()   
    
    fDistance = (nEndTime - nStartTime).microseconds / 29./2.
    return fDistance

GPIO.setmode(GPIO.BCM)

GPIO.setup(TP, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(EP, GPIO.IN)

for i in red:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

for i in green:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
print("initialized")

time.sleep(0.5)
print("hello")



#try:
while(1):
    fDistance = getDistance()
    print(fDistance)
    if fDistance<30:
        print("up")
        for i in green:
            GPIO.output(i, GPIO.LOW)
        for i in red:
            GPIO.output(i, GPIO.HIGH)
        temp_is_parked=1
    else:
        print("down")
        for i in red:
            GPIO.output(i, GPIO.LOW)
        for i in green:
            GPIO.output(i, GPIO.HIGH)
        temp_is_parked=0
    if(is_parked!=temp_is_parked):
        is_parked=temp_is_parked
        params = {'parkinglot_id': parking_lot, "isparked":is_parked ,"parkingspace":parking_space}
        response = requests.post(url = url, data = params)
        print (response.json())
        #print("..")
    time.sleep(5)
#except KeyboardInterrupt:
#    print("KeyboardInterrupt")
#except:
#    print("err")
#finally:
#    GPIO.cleanup()



    
'''
ctrl_interface=DIR=/var/run/wpa_supplicant
GROUP=netdev
update_config=1
coutry=US

network={
    ssid="KT_GIGA_2G_Wave2_2E50"
    psk="fdg1eeh487"
    }
'''
