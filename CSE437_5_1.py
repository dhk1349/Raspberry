#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:46:02 2019

@author: donghoon
"""

import RPi.GPIO as GPIO

import time

usleep=lambda x: time.sleep(x/1000000.0)

import datetime as dt

TP=4
EP=17

def getDistance():
    fDistance = 0.0
    nStartTime, nEndTime=0.0
    
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
time.sleep(0.5)

while(1):
    fDistance = getDistance()
    print(fDistance)
    time.sleep(1)