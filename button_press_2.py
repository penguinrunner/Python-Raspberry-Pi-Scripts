import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # Set pin to be an output pin and set initial value to low (off)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW) # Set pin to be an output pin and set initial value to low (off)

def button_callback_red(channel):
	print("Red!")
	GPIO.output(40, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(40, GPIO.LOW)

def button_callback_green(channel):
	print("Green!")
	GPIO.output(38, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(38, GPIO.LOW)


GPIO.add_event_detect(35,GPIO.RISING,callback=button_callback_green) # Setup event on pin rising edge
GPIO.add_event_detect(37,GPIO.RISING,callback=button_callback_red) # Setup event on pin rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up