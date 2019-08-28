from Adafruit_IO import Client,Feed, Data
import time
import RPi.GPIO as GPIO
import os


ADAFRUIT_IO_KEY = 'd234a59c2c754a7f87be9052f8073018'
ADAFRUIT_IO_USERNAME = 'SasaSaini'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

temperature = aio.feeds('hack.remote')
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


while True:
    data = aio.receive(temperature.key)
    print(data.value)
    if data.value == "10":
        GPIO.output(8, GPIO.HIGH)
    elif data.value == "11":
        GPIO.output(8, GPIO.LOW)
    elif data.value == "12":
        os.system("omxplayer 02TohDishoom.mp3")
        
    time.sleep(0.5)

