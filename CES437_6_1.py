#Import SDK packages
from AWSIoTPython.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("my_id")

myMQTTClient.configureEndpoint()
myMQTTClient.configureCredentials()

myMQTTClient.connect()
for i in range(10):
	myMQTTClient.publish("hello/", "mypayload"+str(i),0)
	myMQTTClent.unsubscire("hello/")
myMQTTClient.disconnect()
