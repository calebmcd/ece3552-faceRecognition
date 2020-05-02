import pi_face_recognition as pfr
import time
import RPi.GPIO as GPIO
import threading

def setup:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    button_state = GPIO.input(11)
    GPIO.add_event_detect(11, GPIO.RISING, callback=cb)

def swButton
    try:
        while True:
            if button_state == False:
                print('Button Pressed')
                time.sleep(0.2)
         
    except:
        GPIO.cleanup()