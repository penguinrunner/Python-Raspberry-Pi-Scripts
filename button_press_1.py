import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

def button_callback_red(channel):
	print("Red!")
	time.sleep(.5)

def button_callback_green(channel):
	print("Green!")
	time.sleep(.5)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 37 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 35 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(35,GPIO.RISING,callback=button_callback_green) # Setup event on pin 35 rising edge
GPIO.add_event_detect(37,GPIO.RISING,callback=button_callback_red) # Setup event on pin 37 rising edge


message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up