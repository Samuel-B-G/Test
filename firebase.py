import requests
import json

# Jag laddar in admin-nyckeln från en annan fil för att den är så lång, man hade bara kunnat förvara den direct i scripten här
file = open("key.txt", "r")
KEY = file.read()
file.close()

# Jag laddar även in device-id från en annan fil, varje device ska ha ett unikt id så jag kände att det var bäst att hämta den från en fil utanför scriptet
file = open("device-id.txt", "r")
DEVICE_ID = file.read()
file.close()

# URL till vår Firebase databas
RTDB = "https://group11-plant4all-default-rtdb.europe-west1.firebasedatabase.app/"

def saveToFirebase(temperature, humidity, light):
	# Här skapar jag ett objekt med den data som skall förvaras i Firebase
	data = {"temperature": temperature,
	"humidity": humidity,
	"light": light}
	# Vi skickar datan till Realtime Database i Firebase, den kommer att förvaras i ett fack namngett efter DEVICE_ID
	response = requests.put(RTDB+"/deviceData/"+DEVICE_ID+".json?auth="+KEY,json=data)
	# Firebase kommer att returnera samma data som vi skrev in, vilket printas ut, denna del kan tas bort
	print(response.json())

# Det är bara att kalla denna funktion för att ladda upp data till Firebase
saveToFirebase(21.5, 31, 216)
