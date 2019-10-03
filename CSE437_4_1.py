#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:26:54 2019

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

def LEDcontrol(keypadnum):
    for i in rangre(8):
        if (i==ketpadnum):
            GPIO.output(REDLEDlist[i], GPIO.HIGH)
        else:
            GPIO.output(REDLEDlist[i], GPIO.LOW)

GPIO.setmode(GPIO.BCM)

for i in REDLEDlist:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
for i in KEYPADlist:
    GPIO.setup(i, GPIO.IN)
time.sleep(0.5)

while(1):
    try:
        keypadnum = keypadRead()
        LEDControl(keypadnum)
    except KeyboardInterrupt:
        pass
GPIO.cleanup()
