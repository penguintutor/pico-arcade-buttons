# pico-arcade-buttons
Simple games using arcade buttons controlled by a Raspberry Pi Pico.

This game was created for [The MagPi issue 129](https://magpi.raspberrypi.com/issues/129) 

# Hardware

This is based around a Raspberry Pi Pico, with arcade buttons, and using a ULN2803 darlington driver to control the LEDs 

For more details see [Raspberry Pi Pico Arcade button quiz game](http://www.penguintutor.com/projects/quiz-game)

# Demo program

File button-buzzer-demo1.py is an example program for testing inputs and outputs from the Raspberry Pi Pico.

# Game files

## quiz-game.py

The quiz game is a fastest to the buzzer multiplayer quiz game. The arcade button that is pressed first lights up and the buzzer sounds.

## reaction-game.py

Multiplayer fastest reaction game using light-up arcade buttons and a Raspberry Pi Pico.

The white arcade button lights up and then the first to press their own button wins that round. 
