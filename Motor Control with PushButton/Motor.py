# import time for delays and RPi.GPIO for GPIO pins
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #set the board mode
GPIO.setwarnings(False) #all warning as false
pin1 =  7 #define pins
pin2 = 11 #define pins
button = 12 #define pins
GPIO.setup(pin1, GPIO.OUT) #define pinmode
GPIO.setup(pin2, GPIO.OUT) #define pinmode
GPIO.setup(button, GPIO.IN, pull_up_down= GPIO.PUD_UP) #define pinmode

# Operation starts
while(1):
    if GPIO.input(button)== GPIO.LOW:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
        time.sleep(0.1)
    else:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.HIGH)
        time.sleep(0.1)