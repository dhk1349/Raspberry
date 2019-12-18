import RPi.GPIO as GPIO
import time
R=6
G=13
B=19

GPIO.setmode(GPIO.BCM)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
while True:
	try:
		red=GPIO.PWM(R,100)
		green=GPIO.PWM(G,100)
		blue=GPIO.PWM(B,100)

		red.start(0)
		green.start(0)
		blue.start(100)
		time.sleep(2)
	except KeyboardInterrupt:
		GPIO.cleanup()
		break
