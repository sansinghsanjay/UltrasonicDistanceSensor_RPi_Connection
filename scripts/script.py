# libraries
import RPi.GPIO as GPIO
import time
 
# GPIO board mode
GPIO.setmode(GPIO.BCM)
 
# GPIO pins
TRIGGER_PIN = 18
ECHO_PIN = 24
 
# set board configurations
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# global vars
start_time = 0
stop_time = 0

# run forever and print distance
while(True):
	# set trigger pin to high - transmit the ultrasonic waves
	GPIO.output(TRIGGER_PIN, True)
	# reset trigger after 0.01 ms
	time.sleep(0.00001)
	GPIO.output(TRIGGER_PIN, False)
	# get start time - not receiving echos
	while(GPIO.input(ECHO_PIN) == 0):
		start_time = time.time()
	# get stop time - as it receives echo
	while(GPIO.input(ECHO_PIN) == 1):
		stop_time = time.time()
	# calculate distance
	distance = ((stop_time - start_time) * 34300) / 2
	# print distance
	print("Distance: ", distance)
	# wait for a second
	time.sleep(1)

