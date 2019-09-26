# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:52:44 2019

@author: dhk13
"""

import RPi.GPIO as GPIO

import time

REDLEDlist=[
        4, 17, 18, 27, 22, 23, 24, 25
        ]

GREENLEDlist=[
         6, 12, 13, 16, 19, 20, 26, 21
        ]

def LEDControl(color):
    if color=="RED":
        for i in range(8):
            GPIO.output(REDLEDlist[i], GPIO.HIGH)
            
            GPIO.output(GREENLEDlist[i], GPIO.LOW)
    elif color=="GREEN":
        for i in range(8):
            GPIO.output(REDLEDlist[i], GPIO.LOW)
            
            GPIO.output(GREENLEDlist[i], GPIO.HIGH)
            
GPIO.setmode(GPIO.BCM)
    
for i in REDLEDlist:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
for i in GREENLEDlist:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
    
time.sleep(0.5)

for i in range(10):
    try:
        LEDControl("RED")
        time.sleep(0.5)
        LEDControl("GREEN")
        time.sleep(0.5)
    except KeyboardInterrupt:
        pass
GPIO.cleanup()
    
    
    
    
    
    