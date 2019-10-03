import RPi.GPIO as GPIO
import time
GPIO.cleanup()

REDLEDlist=[
	4, 17, 18, 27, 22, 23, 24, 25
	]
KEYPADlist=[
	6, 12, 13, 16, 19, 20, 26, 21
	]
Status=[
        False, False, False, False, False, False, False, False 
        ] 


def KeypadRead():
	keypadnum=-1
	for i in range(8):
		if (not GPIO.input(KEYPADlist[i])):
			keypadnum=i
			break
	return keypadnum

def LEDControl(keypadnum, Status):
	if keypadnum!=-1:
                for i in range(8):
                        if(keypadnum==i):
                                GPIO.output(REDLEDlist[i], GPIO.HIGH)
                                Status[i]=True
                        else:
                                GPIO.output(REDLEDlist[i], GPIO.LOW)
	return Status
		


GPIO.setmode(GPIO.BCM)
for i in REDLEDlist:
	GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

for i in KEYPADlist:
	GPIO.setup(i, GPIO.IN)

print("initialized")
time.sleep(0.5)


while(1):
	try:
		keypadnum=KeypadRead()
		Status=LEDControl(keypadnum, Status)
		time.sleep(0.5)
		
	except KeyboardInterrupt:
                GPIO.cleanup()
                pass
		

