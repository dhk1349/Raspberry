import time, json, ssl
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

import time

usleep=lambda x: time.sleep(x/1000000.0)

import datetime as dt

parking_lot="A"
lot=[]

TP=11
EP=10
green=[4, 18, 22, 24, 17, 27, 23, 25]
red=[6, 13, 19, 26, 12, 16, 20, 21]

def getDistance():
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

GPIO.setup(TP, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(EP, GPIO.IN)

for i in red:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

for i in green:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
print("initialized")

time.sleep(0.5)
print("hello")






ENDPOINT = ''
THING_NAME = 'test-thing'

def on_connect(mqttc, obj, flags, rc):
	if rc == 0: #
		print('connected!!')
		mqttc.subscribe('test/2', qos=0) #

def on_message(mqttc, obj, msg):
	if msg.topic == 'test/2':
		payload = msg.payload.decode('utf-8')
		j = json.loads(payload)
		print(j['message'])

mqtt_client = mqtt.Client(client_id=THING_NAME)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.tls_set('./certs/ca.pem', certfile='./certs/cert.pem.crt',
	keyfile='./certs/private.pem.key', tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqtt_client.connect(ENDPOINT, port=8883)
mqtt_client.loop_start() # threaded network loop

try:
    while(1):
        fDistance = getDistance()
        print(fDistance)
        if fDistance<30:
            print("up")
            for i in green:
                GPIO.output(i, GPIO.LOW)
            for i in red:
                GPIO.output(i, GPIO.HIGH)
        
        else:
            print("down")
            for i in red:
                GPIO.output(i, GPIO.LOW)
            for i in green:
                GPIO.output(i, GPIO.HIGH)
        #print("..")
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
except:
    print("err")
finally:
    GPIO.cleanup()

payload = json.dumps({'action': 'test'})
mqtt_client.publish('test/1', payload, qos=1)
