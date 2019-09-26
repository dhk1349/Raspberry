# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:10:40 2019

@author: dhk13
"""
import RPi.GPIO as GPIO

import time

LEDlist=[
         4, 17, 18, 27, 22, 23, 24, 25,
         6, 12, 13, 16, 19, 20, 26, 21
        ]

LEDeven=[
        17, 27, 23, 25, 12, 16, 20, 21
        ]
LEDodd=[
        4, 18, 22, 24, 6, 13, 19, 26 
        ]

GPIO.setmode(GPIO.BCM)

for i in LEDlist:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

for i in LEDodd:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(i, GPIO.LOW)
    time.sleep(0.5)
for i in LEDeven:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(i, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()