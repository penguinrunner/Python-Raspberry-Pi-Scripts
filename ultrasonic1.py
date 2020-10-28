import RPi.GPIO as GPIO
import time

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220  # define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE * 60  # calculate timeout according to the maximum measuring distance

GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
GPIO.setup(trigPin, GPIO.OUT)  # set trigPin to OUTPUT mode
GPIO.setup(echoPin, GPIO.IN)  # set echoPin to INPUT mode


while (True):
	GPIO.output(trigPin, GPIO.HIGH)  # make trigPin output 10us HIGH level
	time.sleep(0.00001)  # 10us
	GPIO.output(trigPin, GPIO.LOW)  # make trigPin output LOW level

	t0 = time.time()
	while (GPIO.input(echoPin) != GPIO.HIGH):
		if ((time.time() - t0) > timeOut * 0.000001):
			pingTime = 0
	t0 = time.time()

	while (GPIO.input(echoPin) == GPIO.HIGH):
		if ((time.time() - t0) > timeOut * 0.000001):
			pingTime = 0
	pingTime = (time.time() - t0) * 1000000

	distance = pingTime * 340.0 / 2.0 / 10000.0  # calculate distance with sound speed 340m/s
	distance = distance * 0.3937007874

	if distance > MAX_DISTANCE:
		distance = MAX_DISTANCE

	print("The distance is : %.2f in" % (distance))
	time.sleep(1)
