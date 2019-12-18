import requests, json
import RPi.GPIO as GPIO
import datetime as dt
import time
from copy import deepcopy

usleep=lambda x: time.sleep(x/1000000.0)
SERVER_URL='http://15.164.246.28'
PARKINGLOT_ID=12
THRESHOLD=12
status=requests.get(SERVER_URL+'/api/parkingspace/list?parkingLot_id={}'.format(PARKINGLOT_ID)).text
status=json.loads(status)['data']
print('intital',status)
pins=[{'TP':4,'EP':17,},{'TP':23,'EP':24},{'TP':6,'EP':12}]



def getDistance(TP,EP):
	fDistance = 0.0
	nStartTime, nEndTime=0,0
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

for i in range(len(pins)):
	GPIO.setup(pins[i]['TP'], GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(pins[i]['EP'], GPIO.IN)

while True:
	temp=deepcopy(status)
	for i in range(len(pins)):
		d=getDistance(pins[i]['TP'],pins[i]['EP'])
		if d<THRESHOLD:
			temp[i]['isFull']=1
		else:
			temp[i]['isFull']=0
		print(round(d),status[i],temp[i])
	time.sleep(1)
	for i in range(len(pins)):
		if temp[i]['isFull']!=status[i]['isFull']:
			print('pre:{}\tcurrent:{}'.format(status[i],temp[i]))
			res=requests.post(SERVER_URL+'/api/parkingspace/update',data=temp[i])
			if res.status_code!=200:
				#print('error occured',res.text)
			status[i]=deepcopy(temp[i])
