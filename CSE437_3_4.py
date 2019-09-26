# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:37:44 2019

@author: dhk13
"""

import RPi.GPIO as GPIO

import time

LEDlist=[
         4, 17, 18, 27, 22, 23, 24, 25,
         6, 12, 13, 16, 19, 20, 26, 21
        ]

GPIO.setmode(GPIO.BCM)

for i in LEDlist:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
    
for i in range(0,len(LEDlist), 2):
    GPIO.OUT(LEDlist[i], GPIO.HIGH)
    GPIO.OUT(LEDlist[i+1], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.OUT(LEDlist[i], GPIO.LOW)
    GPIO.OUT(LEDlist[i+1], GPIO.LOW)    
    time.sleep(0.5)
    


GPIO.cleanup()