#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:42:51 2019

@author: donghoon
"""

import RPi.GPIO as GPIO
import time
REDLEDlist=[
        4, 17, 18, 27, 22, 23, 24, 25
        ]
KEYPADlist=[
        6, 12, 13, 16, 19, 20, 26, 21
        ]

def KeypadRead():
    keypadnum=-1
    for i in range(8):
        if (not GPIO.input(KEYPADlist[i])):
            #GPIO.input()
            keypadnum=i
            break
    return keypadnum

def LEDControl():
    if(keypadnum+1==4):
        for i in REDLEDlist:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(i, GPIO.LOW)
            time.sleep(0.5)
    elif keypadnum+1==5:
        for i in range(8,0,-1):
            GPIO.output(REDLEDlist[i-1], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(REDLEDlist[i-1], GPIO.LOW)            
            time.sleep(0.5)
    else:
        pass

GPIO.setmode(GPIO.BCM)

for i in REDLEDlist:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
for i in KEYPADlist:
    GPIO.setup(i, GPIO.IN)
time.sleep(0.5)

while(1):
    try:
        keypadnum = KeypadRead()
        LEDControl(keypadnum)
    except KeyboardInterrupt:
        pass
GPIO.cleanup()
