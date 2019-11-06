# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 01:20:47 2019

@author: dhk1349
"""

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.out) 
for i in range(0.3):
    GPIO.output(7, True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)
GPIO.cleanup()