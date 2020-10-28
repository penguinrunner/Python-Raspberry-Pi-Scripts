import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import threading

red_button = 37
green_button = 35
red_led = 40
green_led =  38

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(red_led, GPIO.OUT, initial=GPIO.LOW) # Set pin to be an output pin and set initial value to low (off)
GPIO.setup(green_led, GPIO.OUT, initial=GPIO.LOW) # Set pin to be an output pin and set initial value to low (off)


def button_callback_red_on(channel):
	global line1
	GPIO.output(red_led, GPIO.HIGH)
	print("Red On")


def button_callback_red_off(channel):
	global line1
	GPIO.output(red_led, GPIO.LOW)
	print("Red Off")


def button_callback_green_on(channel):
	global line2
	GPIO.output(green_led, GPIO.HIGH)
	print("Green On")

def button_callback_green_off(channel):
	global line2
	GPIO.output(green_led, GPIO.LOW)
	print("Green Off")

def start_red_thread(channel):
	if GPIO.input(red_button) == True:
		red_thread = threading.Thread(target=button_callback_red_on, args={"channel": channel})
	else:
		red_thread = threading.Thread(target=button_callback_red_off, args={"channel": channel})
	red_thread.start()


def start_green_thread(channel):
	if GPIO.input(green_button) == True:
		green_thread = threading.Thread(target=button_callback_green_on,args={"channel":channel})
	else:
		green_thread = threading.Thread(target=button_callback_green_off,args={"channel":channel})
	green_thread.start()


GPIO.add_event_detect(green_button,GPIO.BOTH,callback=start_green_thread) # Setup event on pin rising edge
GPIO.add_event_detect(red_button,GPIO.BOTH,callback=start_red_thread) # Setup event on pin rising edge


message1 = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
