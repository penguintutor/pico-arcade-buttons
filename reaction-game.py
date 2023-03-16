## Reaction game
# White button lights up, then first to react lights up
from machine import Pin
import utime
import random

buzzer = Pin(15, Pin.OUT)
# Red, Green, Yellow, Blue, White
button_pins = [16, 17, 18, 19, 20]
led_pins = [6, 7, 8, 9, 10]
buttons = []
leds = []

white_button_led = Pin(led_pins[4], Pin.OUT)
# start with white LED off
white_button_led.value(4)

# skip last button (white center button)
for i in range (0, len(button_pins)-1):
    buttons.append (Pin(button_pins[i], Pin.IN, Pin.PULL_UP))
    leds.append (Pin(led_pins[i], Pin.OUT))

while (1):
    button_pressed = False
    # Wait random time before lighting button
    utime.sleep(random.randint(1,10))
    white_button_led.value(1)
    # inner while loop to keep checking until button pressed
    while (1):
        # check for which buttons pressed
        for i in range (0, len(buttons)):
            if buttons[i].value() == 0:
                print ("Button {} pressed".format(i))
                leds[i].value(1)
                button_pressed = True
            else:
                leds[i].value(0)
        if button_pressed:
            white_button_led.value(0)
            # Sound buzzer for 0.5 second
            buzzer.value(1)
            utime.sleep(0.5)
            buzzer.value(0)
            # Leave LEDs on for 5 seconds
            utime.sleep(2)
            # Reset all buttons
            for i in range (0, len(buttons)):
                leds[i].value(0)
            # wait at least 2 seconds before next light
            utime.sleep(2)
            break
