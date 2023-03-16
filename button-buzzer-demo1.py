# Test just one button and LED
from machine import Pin
import utime

button = Pin(16, Pin.IN, Pin.PULL_UP)
output = Pin(15, Pin.OUT)

while (1):
    if (button.value() == 0):
        output.value(1)
    else:
        output.value(0)
