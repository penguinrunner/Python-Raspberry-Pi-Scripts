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

def button_callback_red(channel):
	print("Red!")
	GPIO.output(red_led, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(red_led, GPIO.LOW)

def button_callback_green(channel):
	print("Green!")
	GPIO.output(green_led, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(green_led, GPIO.LOW)

def start_red_thread(channel):
	red_thread = threading.Thread(target=button_callback_red,args={"channel":channel})
	red_thread.start()
	print("RED thread started")

def start_green_thread(channel):
	green_thread = threading.Thread(target=button_callback_green,args={"channel":channel})
	green_thread.start()
	print("RED thread started")


GPIO.add_event_detect(green_button,GPIO.RISING,callback=start_green_thread) # Setup event on pin rising edge
GPIO.add_event_detect(37,GPIO.RISING,callback=start_red_thread) # Setup event on pin rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
