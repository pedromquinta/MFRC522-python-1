#!/usr/bin/env python

import RPi.GPIO as GPIO
from gpiozero import Button, Buzzer
from time import sleep
from mfrc522 import SimpleMFRC522
import sys

GPIO.setwarnings(False)

sw1 = Button(21)
sw2 = Button(16)
sw3 = Button(20)
buzzer = Buzzer(26)

reader = SimpleMFRC522()

buzzer.beep(0.1, 0.1, 2)

try:
    while True:
        if sw1.is_pressed:
            print("Hold a tag near the reader")
            id, text = reader.read()
            buzzer.beep(0.1, 0.1, 1)
            print("ID: %s\nText: %s" % (id,text))
            print()
        
        elif sw2.is_pressed:
            text = input('New data:')
            print("Now place your tag to write")
            reader.write(text)
            buzzer.beep(0.1, 0.1, 1)
            print("Written")
            print()

except KeyboardInterrupt:
    GPIO.cleanup()
    raise