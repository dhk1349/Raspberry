#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:26:54 2019

@author: donghoon
"""

import RPi.GPIO as GPIO
import time
REDLEDlist=[
        16, 20, 21, 7, 8, 25
        ]
#15, 

GPIO.setmode(GPIO.BCM)
for i in REDLEDlist:
	GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
	
print("initialized")
time.sleep(0.5)

while True:
        for i in range(len(REDLEDlist)):
            GPIO.output(REDLEDlist[i], GPIO.HIGH)
        time.sleep(1)
        for i in range(len(REDLEDlist)):
            GPIO.output(REDLEDlist[i], GPIO.LOW)
        time.sleep(1)
