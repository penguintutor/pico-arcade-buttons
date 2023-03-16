## Quiz game
# Detects the first to press their button
# Sounds the buzzer for 1 second and lights the
# button pressed for additional 2 seconds
from machine import Pin
import utime

buzzer = Pin(15, Pin.OUT)
# Red, Green, Yellow, Blue, White
button_pins = [16, 17, 18, 19, 20]
led_pins = [6, 7, 8, 9, 10]
buttons = []
leds = []

for i in range (0, len(button_pins)):
    buttons.append (Pin(button_pins[i], Pin.IN, Pin.PULL_UP))
    leds.append (Pin(led_pins[i], Pin.OUT))

while (1):
    button_pressed = False
    # check for which buttons pressed
    for i in range (0, len(buttons)):
        if buttons[i].value() == 0:
            print ("Button {} pressed".format(i))
            leds[i].value(1)
            button_pressed = True
        else:
            leds[i].value(0)
    if button_pressed:
        # Sound buzzer for 1 second
        buzzer.value(1)
        utime.sleep(1)
        buzzer.value(0)
        # Leave LEDs on for 2 more seconds
        utime.sleep(2)
        # Reset all buttons
        for i in range (0, len(buttons)):
            buttons[i].value(0)
