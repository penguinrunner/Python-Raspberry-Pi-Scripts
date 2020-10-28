import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(40, GPIO.HIGH) # Turn on
 GPIO.output(38, GPIO.LOW) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(40, GPIO.LOW) # Turn off
 GPIO.output(38, GPIO.HIGH) # Turn off
 sleep(1) # Sleep for 1 second