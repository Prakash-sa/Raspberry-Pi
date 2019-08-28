
import bluetooth
import RPi.GPIO as GPIO

led_pin = 21	
GPIO.setmode(GPIO.BCM)	
GPIO.setup(led_pin, GPIO.OUT)	

host = ""
port = 1


server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')

try:
	server.bind((host, port))
	print("Bluetooth Binding Completed")
except:
	print("Bluetooth Binding Failed")

server.listen(1) 
client, address = server.accept()
print("Connected To", address)
print("Client:", client)

try:
	while True:

		data = client.recv(1024) 
		print(data)
		
		if data == "1":
			GPIO.output(led_pin, True)
			send_data = "Light On "
		elif data == "0":
			GPIO.output(led_pin, False)
			send_data = "Light Off "
		else:
			send_data = "Type 1 or 0 "
		client.send(send_data) 
except:
	GPIO.cleanup()
	client.close()
	server.close()