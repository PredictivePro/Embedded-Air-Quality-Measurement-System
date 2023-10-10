#importing the required libraries
import dht11
import RPi.GPIO as RPi

def measure_temp_hum():
    #initialize GPIO
    RPi.setwarnings(False)
    RPi.setmode(RPi.BCM)
    RPi.cleanup()

    while True:
        # To read data using pin 4
        RPi.setmode(RPi.BCM)
        instance = dht11.DHT11(pin=4)
        result = instance.read()
        while not result.is_valid(): # read until valid values
            result = instance.read()

        #To print current temperature and humidity on the console.
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)

        current_temp = result.temperature
        current_hum = result.humidity

        current_atmospheric_values = [current_temp, current_hum]  # The current values are stored in the form of a list
        # to be returned.

        return current_atmospheric_values



