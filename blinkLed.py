import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

def blink():
  GPIO.output(18, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(18, GPIO.LOW)
  time.sleep(1)

for i in range(0, 9):
  blink()
