import requests
import json

file = open("key.txt", "r")
KEY = file.read()
file.close()

file = open("device-id.txt", "r")
DEVICE_ID = file.read()
file.close()
print(DEVICE_ID)
print(DEVICE_ID)
print(len(DEVICE_ID))
RTDB = "https://group11-plant4all-default-rtdb.europe-west1.firebasedatabase.app/"

def saveToFirebase(temperature, humidity, light):
	data = {"temperature": temperature,
	"humidity": humidity,
	"light": light}
	response = requests.put(RTDB+"/deviceData/"+DEVICE_ID+".json?auth="+KEY,json=data)
	print(response.json())

saveToFirebase(21.5, 31, 216)
