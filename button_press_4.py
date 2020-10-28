import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import threading
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

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

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
	mcp = PCF8574_GPIO(PCF8574_address)
except:
	try:
		mcp = PCF8574_GPIO(PCF8574A_address)
	except:
		print('I2C Address Error !')
		exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)

mcp.output(3, 1)  # turn on LCD backlight
lcd.begin(16, 2)  # set number of LCD lines and columns

message = ""
line1 = "Red Off"
line2 = "Green Off"


def set_message():
	lcd.clear()
	lcd.setCursor(0, 0)  # set cursor position
	lcd.message("    "+line1)  # display the time
	lcd.message("\n")  # New Line
	lcd.message("    "+line2)  # display the time


def button_callback_red(channel):
	print("Red!")
	global line1
	GPIO.output(red_led, GPIO.HIGH)
	line1 = "Red On"
	set_message()
	time.sleep(.5)
	line1 = "Red Off"
	lcd.clear()
	set_message()
	GPIO.output(red_led, GPIO.LOW)

def button_callback_green(channel):
	print("Green!")
	global line2
	GPIO.output(green_led, GPIO.HIGH)
	line2 = "Green On"
	set_message()
	time.sleep(.5)
	line2 = "Green Off"
	set_message()
	GPIO.output(green_led, GPIO.LOW)

def start_red_thread(channel):
	red_thread = threading.Thread(target=button_callback_red,args={"channel":channel})
	red_thread.start()

def start_green_thread(channel):
	green_thread = threading.Thread(target=button_callback_green,args={"channel":channel})
	green_thread.start()

set_message()
GPIO.add_event_detect(green_button,GPIO.RISING,callback=start_green_thread) # Setup event on pin rising edge
GPIO.add_event_detect(37,GPIO.RISING,callback=start_red_thread) # Setup event on pin rising edge

message1 = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
lcd.clear()